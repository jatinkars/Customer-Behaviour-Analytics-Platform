from __future__ import annotations
import pandas as pd
from sqlalchemy import text
from ..utils.db import get_engine

def get_daily_kpis(limit: int = 30) -> pd.DataFrame:
    engine = get_engine()
    q = text("SELECT * FROM analytics.vw_kpis_daily ORDER BY activity_date DESC LIMIT :limit;")
    return pd.read_sql(q, engine, params={"limit": limit})

if __name__ == "__main__":
    print(get_daily_kpis(10))
