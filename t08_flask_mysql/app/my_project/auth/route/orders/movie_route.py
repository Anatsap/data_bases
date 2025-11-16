
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import actor_controller
from t08_flask_mysql.app.my_project.auth.domain import Movie

movie_bp = Blueprint('movies', __name__, url_prefix='/movies')


@movie_bp.get('')
def get_all_movies() -> Response:
    return make_response(jsonify(actor_controller.find_all()), HTTPStatus.OK)


@movie_bp.post('')
def create_movie() -> Response:
    content = request.get_json()
    movie = Movie.create_from_dto(content)
    actor_controller.create(movie)
    return make_response(jsonify(movie.put_into_dto()), HTTPStatus.CREATED)


@movie_bp.get('/<int:movie_id>')
def get_movie(movie_id: int) -> Response:
    return make_response(jsonify(actor_controller.find_by_id(movie_id)), HTTPStatus.OK)


@movie_bp.put('/<int:movie_id>')
def update_movie(movie_id: int) -> Response:
    content = request.get_json()
    movie = Movie.create_from_dto(content)
    actor_controller.update(movie_id, movie)
    return make_response("Movie updated", HTTPStatus.OK)


@movie_bp.patch('/<int:movie_id>')
def patch_movie(movie_id: int) -> Response:
    content = request.get_json()
    actor_controller.patch(movie_id, content)
    return make_response("Movie updated", HTTPStatus.OK)


@movie_bp.delete('/<int:movie_id>')
def delete_movie(movie_id: int) -> Response:
    actor_controller.delete(movie_id)
    return make_response("Movie deleted", HTTPStatus.OK)

@movie_bp.route('/<int:movie_id>/actors', methods=['GET'])
def get_movie_actors(movie_id: int) -> Response:
    actors_dto_list = actor_controller.get_actors_by_movie_id_route(movie_id)
    return make_response(jsonify(actors_dto_list), HTTPStatus.OK)

