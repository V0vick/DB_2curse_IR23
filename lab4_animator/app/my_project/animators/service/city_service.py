from typing import List, Optional
from my_project.animators.dao.city_dao import CityDAO
from my_project.animators.domain.city import City


class CityService:
    def __init__(self, dao: Optional[CityDAO] = None):
        self.dao = dao or CityDAO()

    def get_all_cities(self) -> List[dict]:
        return [city.to_dict() for city in self.dao.get_all()]

    def get_city_by_id(self, city_id: int) -> Optional[dict]:
        city = self.dao.get_by_id(city_id)
        return city.to_dict() if city else None

    def create_city(self, data: dict) -> dict:
        name = (data or {}).get("name", "").strip()
        if not name:
            raise ValueError("City name is required")
        created = self.dao.create(City(name=name))
        return created.to_dict()

    def update_city(self, city_id: int, data: dict) -> Optional[dict]:
        name = (data or {}).get("name", "").strip()
        if not name:
            raise ValueError("City name is required")
        updated = self.dao.update(city_id, City(name=name))
        return updated.to_dict() if updated else None

    def delete_city(self, city_id: int) -> bool:
        return self.dao.delete(city_id)