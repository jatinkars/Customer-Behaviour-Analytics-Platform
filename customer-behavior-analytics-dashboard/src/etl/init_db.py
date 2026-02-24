from __future__ import annotations
from pathlib import Path
from sqlalchemy.engine import Engine
from ..utils.db import run_sql_file
from ..utils.log import get_logger

logger = get_logger(__name__)

def init_db(engine: Engine) -> None:
    logger.info("Initializing schemas...")
    run_sql_file(engine, str(Path("sql/01_schema.sql")))
    logger.info("Creating staging tables...")
    run_sql_file(engine, str(Path("sql/02_staging.sql")))
    logger.info("DB initialized.")
