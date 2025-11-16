
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import review_controller
from t08_flask_mysql.app.my_project.auth.domain import Review

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@review_bp.get('')
def get_all_reviews() -> Response:
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)


@review_bp.post('')
def create_review() -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@review_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:
    review_obj = review_controller.find_by_id(review_id)
    if review_obj:
        return make_response(jsonify(review_obj.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Review not found"}), HTTPStatus.NOT_FOUND)


@review_bp.put('/<int:review_id>')
def update_review(review_id: int) -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.update(review_id, review)
    return make_response(jsonify({"message": f"Review {review_id} updated"}), HTTPStatus.OK)


@review_bp.patch('/<int:review_id>')
def patch_review(review_id: int) -> Response:
    content = request.get_json()
    review_controller.patch(review_id, content)
    return make_response(jsonify({"message": f"Review {review_id} patched"}), HTTPStatus.OK)


@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:
    review_controller.delete(review_id)
    return make_response(jsonify({"message": f"Review {review_id} deleted"}), HTTPStatus.NO_CONTENT)


@review_bp.route('/<int:review_id>/movie', methods=['GET'])
def get_review_movie(review_id: int) -> Response:
    movie_data = review_controller.get_movie_by_review_id_route(review_id)
    return make_response(jsonify(movie_data), HTTPStatus.OK)