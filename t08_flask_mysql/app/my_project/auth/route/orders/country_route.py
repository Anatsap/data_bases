from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import country_controller
from my_project.auth.domain.orders.country import Country



country_bp = Blueprint('countries', __name__, url_prefix='/countries')


@country_bp.get('')
def get_all_countries() -> Response:
    return make_response(jsonify(country_controller.find_all()), HTTPStatus.OK)


@country_bp.post('')
def create_country() -> Response:
    content = request.get_json()
    country = Country.create_from_dto(content)
    country_controller.create(country)
    return make_response(jsonify(country.put_into_dto()), HTTPStatus.CREATED)


@country_bp.get('/<int:country_id>')
def get_country(country_id: int) -> Response:
    return make_response(jsonify(country_controller.find_by_id(country_id)), HTTPStatus.OK)


@country_bp.put('/<int:country_id>')
def update_country(country_id: int) -> Response:
    content = request.get_json()
    country = Country.create_from_dto(content)
    country_controller.update(country_id, country)
    return make_response("Country updated", HTTPStatus.OK)


@country_bp.patch('/<int:country_id>')
def patch_country(country_id: int) -> Response:
    content = request.get_json()
    country_controller.patch(country_id, content)
    return make_response("Country updated", HTTPStatus.OK)
    


@country_bp.delete('/<int:country_id>')
def delete_country(country_id: int) -> Response:
    country_controller.delete(country_id)
    return make_response(jsonify({"message": f"Country {country_id} deleted"}), HTTPStatus.NO_CONTENT)


@country_bp.route('/<int:country_id>/box_office', methods=['GET'])
def get_country_box_office(country_id: int) -> Response:
    box_office_data = country_controller.get_box_office_by_county_route(country_id)
    return make_response(jsonify(box_office_data), HTTPStatus.OK)