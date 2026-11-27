from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class CityAnimatorsDTO:
    city_id: int
    city_name: str
    animators: List[dict]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ProgramDTO:
    id: int
    title: str
    duration_minutes: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class AnimatorProgramsDTO:
    animator_id: int
    animator_name: str
    city_name: Optional[str]
    programs: List[dict]

    def to_dict(self) -> dict:
        return asdict(self)