from flask import Blueprint, jsonify

# agregado de rotas
user_routes_bp = Blueprint("user_routes", __name__)


@user_routes_bp.route("/user", methods=["POST"])
def registry_user():
    # logica e componentes que vão ajudar nas construções depois
    return jsonify({"rota": "Rota de cadastro estou dentro!"}), 200
