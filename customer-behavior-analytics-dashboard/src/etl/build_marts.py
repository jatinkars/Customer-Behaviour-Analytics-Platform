from __future__ import annotations
from pathlib import Path
from sqlalchemy.engine import Engine
from ..utils.db import run_sql_file
from ..utils.log import get_logger

logger = get_logger(__name__)

def build_marts(engine: Engine) -> None:
    logger.info("Building marts: analytics.fact_session, analytics.fact_user_daily, analytics.cohort_retention_weekly")
    run_sql_file(engine, str(Path("sql/03_marts.sql")))
    logger.info("Creating views: analytics.vw_kpis_daily")
    run_sql_file(engine, str(Path("sql/04_views.sql")))
    logger.info("Marts built.")
