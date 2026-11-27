from dataclasses import dataclass
from typing import Optional


@dataclass
class Animator:
    id: Optional[int] = None
    name: str = ""
    specialization: str = ""
    hourly_rate: float = 0.0
    city_id: Optional[int] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "hourly_rate": self.hourly_rate,
            "city_id": self.city_id,
        }