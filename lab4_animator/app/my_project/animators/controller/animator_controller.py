from flask import jsonify, request
from my_project.animators.service.animator_service import AnimatorService


class AnimatorController:
    def __init__(self, service: AnimatorService | None = None):
        self.service = service or AnimatorService()

    def get_all(self):
        return jsonify(self.service.get_all_animators()), 200

    def get_by_id(self, animator_id: int):
        item = self.service.get_animator_by_id(animator_id)
        if not item:
            return jsonify({"error": "Animator not found"}), 404
        return jsonify(item), 200

    def create(self):
        try:
            item = self.service.create_animator(request.get_json(silent=True))
            return jsonify(item), 201
        except (ValueError, TypeError) as exc:
            return jsonify({"error": str(exc)}), 400

    def update(self, animator_id: int):
        try:
            item = self.service.update_animator(animator_id, request.get_json(silent=True))
            if not item:
                return jsonify({"error": "Animator not found"}), 404
            return jsonify(item), 200
        except (ValueError, TypeError) as exc:
            return jsonify({"error": str(exc)}), 400

    def delete(self, animator_id: int):
        deleted = self.service.delete_animator(animator_id)
        if not deleted:
            return jsonify({"error": "Animator not found"}), 404
        return "", 204

    def get_by_city(self, city_id: int):
        dto = self.service.get_animators_by_city_dto(city_id)
        if not dto:
            return jsonify({"error": "City not found"}), 404
        return jsonify(dto), 200

    def get_programs(self, animator_id: int):
        dto = self.service.get_animator_programs_dto(animator_id)
        if not dto:
            return jsonify({"error": "Animator not found"}), 404
        return jsonify(dto), 200