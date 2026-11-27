from pathlib import Path
import mysql.connector
import yaml


def _load_db_config() -> dict:
    config_path = Path(__file__).resolve().parent.parent.parent / "config" / "app.yml"
    with config_path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}
    return data.get("database", {})


def get_db_connection():
    db_cfg = _load_db_config()
    return mysql.connector.connect(
        host=db_cfg.get("host", "localhost"),
        port=int(db_cfg.get("port", 3306)),
        user=db_cfg.get("user", "root"),
        password=db_cfg.get("password", ""),
        database=db_cfg.get("name", "animator_booking_db"),
    )