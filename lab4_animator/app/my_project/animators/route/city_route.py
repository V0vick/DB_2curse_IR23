from flask import Blueprint
from my_project.animators.controller.city_controller import CityController

city_bp = Blueprint("cities", __name__, url_prefix="/api/cities")
controller = CityController()

city_bp.add_url_rule("", view_func=controller.get_all, methods=["GET"])
city_bp.add_url_rule("/<int:city_id>", view_func=controller.get_by_id, methods=["GET"])
city_bp.add_url_rule("", view_func=controller.create, methods=["POST"])
city_bp.add_url_rule("/<int:city_id>", view_func=controller.update, methods=["PUT"])
city_bp.add_url_rule("/<int:city_id>", view_func=controller.delete, methods=["DELETE"])