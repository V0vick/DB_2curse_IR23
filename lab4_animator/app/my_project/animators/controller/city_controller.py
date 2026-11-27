from flask import jsonify, request
from my_project.animators.service.city_service import CityService


class CityController:
    def __init__(self, service: CityService | None = None):
        self.service = service or CityService()

    def get_all(self):
        return jsonify(self.service.get_all_cities()), 200

    def get_by_id(self, city_id: int):
        city = self.service.get_city_by_id(city_id)
        if not city:
            return jsonify({"error": "City not found"}), 404
        return jsonify(city), 200

    def create(self):
        try:
            city = self.service.create_city(request.get_json(silent=True))
            return jsonify(city), 201
        except ValueError as exc:
            return jsonify({"error": str(exc)}), 400

    def update(self, city_id: int):
        try:
            city = self.service.update_city(city_id, request.get_json(silent=True))
            if not city:
                return jsonify({"error": "City not found"}), 404
            return jsonify(city), 200
        except ValueError as exc:
            return jsonify({"error": str(exc)}), 400

    def delete(self, city_id: int):
        deleted = self.service.delete_city(city_id)
        if not deleted:
            return jsonify({"error": "City not found"}), 404
        return "", 204