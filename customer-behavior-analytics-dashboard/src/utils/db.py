from __future__ import annotations
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from .config import settings

def get_engine() -> Engine:
    return create_engine(settings.sqlalchemy_url, pool_pre_ping=True)

def run_sql_file(engine: Engine, path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()
    with engine.begin() as conn:
        conn.execute(text(sql))
