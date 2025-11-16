
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import actor_controller
from t08_flask_mysql.app.my_project.auth.domain import Actor

actor_bp = Blueprint('actors', __name__, url_prefix='/actors')


@actor_bp.get('')
def get_all_actors() -> Response:
    return make_response(jsonify(actor_controller.find_all()), HTTPStatus.OK)


@actor_bp.post('')
def create_actor() -> Response:
    content = request.get_json()
    actor = Actor.create_from_dto(content)
    actor_controller.create(actor)
    return make_response(jsonify(actor.put_into_dto()), HTTPStatus.CREATED)


@actor_bp.get('/<int:actor_id>')
def get_actor(actor_id: int) -> Response:
    return make_response(jsonify(actor_controller.find_by_id(actor_id)), HTTPStatus.OK)


@actor_bp.put('/<int:actor_id>')
def update_actor(actor_id: int) -> Response:
    content = request.get_json()
    actor = Actor.create_from_dto(content)
    actor_controller.update(actor_id, actor)
    return make_response("Actor updated", HTTPStatus.OK)


@actor_bp.patch('/<int:actor_id>')
def patch_actor(actor_id: int) -> Response:
    content = request.get_json()
    actor_controller.patch(actor_id, content)
    return make_response("Actor updated", HTTPStatus.OK)


@actor_bp.delete('/<int:actor_id>')
def delete_actor(actor_id: int) -> Response:
    actor_controller.delete(actor_id)
    return make_response("Actor deleted", HTTPStatus.OK)

@actor_bp.route('/<int:actor_id>/actors', methods=['GET'])
def get_actor_movies(actor_id: int) -> Response:
    movies_data = actor_controller.get_movies_by_actor_id_route(actor_id)
    return make_response(jsonify(movies_data), HTTPStatus.OK)

@actor_bp.route('/nationality/<string:nationality>', methods=['GET'])
def get_actors_nationality(nationality: str) -> Response:
    nat_data = actor_controller.get_actor_by_nationality_route(nationality)
    return make_response(jsonify(nat_data), HTTPStatus.OK)




