import os
import secrets
from http import HTTPStatus
from typing import Dict, Any

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from .auth.route import register_routes

# Database object
db = SQLAlchemy()
todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    _process_input_config(app_config, additional_config)

    app = Flask(__name__)

    app.config["SECRET_KEY"] = secrets.token_hex(16)

    for key, value in app_config.items():
        app.config[key] = value

    _init_db(app)

    register_routes(app)

    _init_swagger(app)

    return app


def _init_swagger(app: Flask) -> None:
    """
    Swagger / RESTX initialization
    """
    restx_api = Api(
        app,
        title="Pavelchak test backend",
        description="A simple backend"
    )

    @restx_api.route('/number/<string:todo_id>')
    class TodoSimple(Resource):
        @staticmethod
        def get(todo_id):
            return todos, HTTPStatus.ACCEPTED

        @staticmethod
        def put(todo_id):
            todos[todo_id] = todo_id
            return todos, HTTPStatus.CREATED

    @app.route("/hi")
    def hello_world():
        return todos, HTTPStatus.OK


def _init_db(app: Flask) -> None:
    """
    Initializes SQLAlchemy and creates DB
    """
    db.init_app(app)

    uri = app.config["SQLALCHEMY_DATABASE_URI"]

    if not database_exists(uri):
        create_database(uri)

    # FIX: правильний імпорт domain-моделей
    import my_project.auth.domain

    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes config and injects DB credentials
    """
    root_user = os.getenv("MYSQL_ROOT_USER", additional_config["MYSQL_ROOT_USER"])
    root_password = os.getenv("MYSQL_ROOT_PASSWORD", additional_config["MYSQL_ROOT_PASSWORD"])

    # Format URI
    app_config["SQLALCHEMY_DATABASE_URI"] = app_config["SQLALCHEMY_DATABASE_URI"].format(
        root_user, root_password
    )
