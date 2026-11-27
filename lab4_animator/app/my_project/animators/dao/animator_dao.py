from typing import List, Optional
from my_project.animators.domain.animator import Animator
from my_project.utils.db import get_db_connection


class AnimatorDAO:
    def _map_row(self, row: dict) -> Animator:
        full_name = f"{row.get('first_name', '')} {row.get('last_name', '')}".strip()
        return Animator(
            id=row["animator_id"],
            name=full_name,
            specialization="",
            hourly_rate=0.0,
            city_id=row.get("city_id"),
        )

    def get_all(self) -> List[Animator]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT animator_id, first_name, last_name, phone, birth_date, experience_years
                FROM animator
                ORDER BY animator_id
                """
            )
            rows = cursor.fetchall()
            return [self._map_row(row) for row in rows]
        finally:
            conn.close()

    def get_by_id(self, animator_id: int) -> Optional[Animator]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT animator_id, first_name, last_name, phone, birth_date, experience_years
                FROM animator
                WHERE animator_id = %s
                """,
                (animator_id,),
            )
            row = cursor.fetchone()
            if not row:
                return None
            return self._map_row(row)
        finally:
            conn.close()

    def get_by_city_id(self, city_id: int) -> List[Animator]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT DISTINCT
                    a.animator_id,
                    a.first_name,
                    a.last_name,
                    a.phone,
                    a.birth_date,
                    a.experience_years,
                    ag.city_id
                FROM animator a
                INNER JOIN agency_animator aa ON aa.animator_id = a.animator_id
                INNER JOIN agency ag ON ag.agency_id = aa.agency_id
                WHERE ag.city_id = %s
                ORDER BY a.animator_id
                """,
                (city_id,),
            )
            rows = cursor.fetchall()
            return [self._map_row(row) for row in rows]
        finally:
            conn.close()

    def get_programs_by_animator_id(self, animator_id: int) -> List[dict]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT
                    s.skill_id AS id,
                    s.skill_name AS title,
                    60 AS duration_minutes
                FROM animator_skill askill
                INNER JOIN skill s ON s.skill_id = askill.skill_id
                WHERE askill.animator_id = %s
                ORDER BY s.skill_id
                """,
                (animator_id,),
            )
            return cursor.fetchall()
        finally:
            conn.close()