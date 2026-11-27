from dataclasses import dataclass
from typing import Optional


@dataclass
class City:
    id: Optional[int] = None
    name: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
        }