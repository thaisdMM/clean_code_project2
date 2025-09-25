from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.user_creator_composer import user_creator_composer
from src.main.composer.user_finder_composer import user_finder_composer

# agregado de rotas
user_routes_bp = Blueprint("user_routes", __name__)


@user_routes_bp.route("/user", methods=["POST"])
def registry_user():
    # logica e componentes que vão ajudar nas construções depois
    http_request = HttpRequest(body=request.json)

    user_creator = user_creator_composer()
    http_response = user_creator.handler_insert_new_user(http_request)

    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route("/user/find/<person_name>", methods=["GET"])
def find_user(person_name):

    http_request = HttpRequest(param={"person_name": person_name})

    user_finder = user_finder_composer()
    http_response = user_finder.handler_find_by_person_name(http_request)

    return jsonify(http_response.body), http_response.status_code
