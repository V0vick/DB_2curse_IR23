from typing import List, Optional
from my_project.animators.domain.city import City
from my_project.utils.db import get_db_connection


class CityDAO:
    def get_all(self) -> List[City]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT city_id, city_name FROM city ORDER BY city_id")
            rows = cursor.fetchall()
            return [City(id=row["city_id"], name=row["city_name"]) for row in rows]
        finally:
            conn.close()

    def get_by_id(self, city_id: int) -> Optional[City]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT city_id, city_name FROM city WHERE city_id = %s",
                (city_id,),
            )
            row = cursor.fetchone()
            if not row:
                return None
            return City(id=row["city_id"], name=row["city_name"])
        finally:
            conn.close()

    def create(self, city: City) -> City:
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO city (city_name) VALUES (%s)", (city.name,))
            conn.commit()
            city.id = cursor.lastrowid
            return city
        finally:
            conn.close()

    def update(self, city_id: int, city: City) -> Optional[City]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE city SET city_name = %s WHERE city_id = %s",
                (city.name, city_id),
            )
            conn.commit()
            if cursor.rowcount == 0:
                return None
            city.id = city_id
            return city
        finally:
            conn.close()

    def delete(self, city_id: int) -> bool:
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM city WHERE city_id = %s", (city_id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()