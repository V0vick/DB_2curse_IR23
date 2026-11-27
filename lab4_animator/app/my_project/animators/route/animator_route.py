from flask import Blueprint
from my_project.animators.controller.animator_controller import AnimatorController

animator_bp = Blueprint("animators", __name__, url_prefix="/api/animators")
controller = AnimatorController()

animator_bp.add_url_rule("", view_func=controller.get_all, methods=["GET"])
animator_bp.add_url_rule("/<int:animator_id>", view_func=controller.get_by_id, methods=["GET"])
animator_bp.add_url_rule("", view_func=controller.create, methods=["POST"])
animator_bp.add_url_rule("/<int:animator_id>", view_func=controller.update, methods=["PUT"])
animator_bp.add_url_rule("/<int:animator_id>", view_func=controller.delete, methods=["DELETE"])
animator_bp.add_url_rule("/by-city/<int:city_id>", view_func=controller.get_by_city, methods=["GET"])
animator_bp.add_url_rule("/<int:animator_id>/programs", view_func=controller.get_programs, methods=["GET"])