from typing import List, Optional
from my_project.animators.dao.animator_dao import AnimatorDAO
from my_project.animators.domain.animator import Animator
from typing import Optional
from my_project.animators.dao.city_dao import CityDAO
from my_project.animators.domain.dto import AnimatorProgramsDTO, CityAnimatorsDTO, ProgramDTO

class AnimatorService:
    def __init__(self, dao: Optional[AnimatorDAO] = None):
        self.dao = dao or AnimatorDAO()

    def get_all_animators(self) -> List[dict]:
        return [item.to_dict() for item in self.dao.get_all()]

    def get_animator_by_id(self, animator_id: int) -> Optional[dict]:
        item = self.dao.get_by_id(animator_id)
        return item.to_dict() if item else None

    def create_animator(self, data: dict) -> dict:
        payload = data or {}
        name = str(payload.get("name", "")).strip()
        if not name:
            raise ValueError("Animator name is required")

        specialization = str(payload.get("specialization", "")).strip()
        hourly_rate = float(payload.get("hourly_rate", 0.0))
        city_id = payload.get("city_id")
        if city_id is not None:
            city_id = int(city_id)

        created = self.dao.create(
            Animator(
                name=name,
                specialization=specialization,
                hourly_rate=hourly_rate,
                city_id=city_id,
            )
        )
        return created.to_dict()

    def update_animator(self, animator_id: int, data: dict) -> Optional[dict]:
        payload = data or {}
        name = str(payload.get("name", "")).strip()
        if not name:
            raise ValueError("Animator name is required")

        specialization = str(payload.get("specialization", "")).strip()
        hourly_rate = float(payload.get("hourly_rate", 0.0))
        city_id = payload.get("city_id")
        if city_id is not None:
            city_id = int(city_id)

        updated = self.dao.update(
            animator_id,
            Animator(
                name=name,
                specialization=specialization,
                hourly_rate=hourly_rate,
                city_id=city_id,
            ),
        )
        return updated.to_dict() if updated else None

    def delete_animator(self, animator_id: int) -> bool:
        return self.dao.delete(animator_id)

    def get_animators_by_city_dto(self, city_id: int) -> Optional[dict]:
        city_dao = CityDAO()
        city = city_dao.get_by_id(city_id)
        if not city:
            return None

        animators = [item.to_dict() for item in self.dao.get_by_city_id(city_id)]
        dto = CityAnimatorsDTO(
            city_id=city.id,
            city_name=city.name,
            animators=animators,
        )
        return dto.to_dict()

    def get_animator_programs_dto(self, animator_id: int) -> Optional[dict]:
        animator = self.dao.get_by_id(animator_id)
        if not animator:
            return None

        city_name = None
        if animator.city_id is not None:
            city = CityDAO().get_by_id(animator.city_id)
            city_name = city.name if city else None

        raw_programs = self.dao.get_programs_by_animator_id(animator_id)
        programs = [
            ProgramDTO(
                id=row["id"],
                title=row["title"],
                duration_minutes=int(row["duration_minutes"]),
            ).to_dict()
            for row in raw_programs
        ]

        dto = AnimatorProgramsDTO(
            animator_id=animator.id,
            animator_name=animator.name,
            city_name=city_name,
            programs=programs,
        )
        return dto.to_dict()