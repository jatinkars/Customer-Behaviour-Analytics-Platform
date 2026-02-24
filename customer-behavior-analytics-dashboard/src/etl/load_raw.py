from __future__ import annotations
from pathlib import Path
import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Engine
from ..utils.config import settings
from ..utils.log import get_logger

logger = get_logger(__name__)

def load_csv_to_table(engine: Engine, csv_path: str, table: str) -> None:
    df = pd.read_csv(csv_path)
    df.to_sql(table.split(".")[-1], engine, schema=table.split(".")[0], if_exists="append", index=False, method="multi", chunksize=5000)

def truncate_tables(engine: Engine) -> None:
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE staging.events CASCADE;"))
        conn.execute(text("TRUNCATE TABLE staging.users CASCADE;"))

def load_raw(engine: Engine) -> None:
    raw_dir = Path(settings.raw_data_dir)
    users_csv = raw_dir / "users.csv"
    events_csv = raw_dir / "events.csv"
    if not users_csv.exists() or not events_csv.exists():
        raise FileNotFoundError(f"Missing raw CSVs in {raw_dir}. Run: python -m src.cli generate-data --rows 100000")

    logger.info("Truncating staging tables...")
    truncate_tables(engine)

    logger.info("Loading users.csv → staging.users")
    load_csv_to_table(engine, str(users_csv), "staging.users")

    logger.info("Loading events.csv → staging.events")
    load_csv_to_table(engine, str(events_csv), "staging.events")

    logger.info("Raw load complete.")
