from __future__ import annotations
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    host: str = os.getenv("DB_HOST", "localhost")
    port: int = int(os.getenv("DB_PORT", "5432"))
    name: str = os.getenv("DB_NAME", "cba_db")
    user: str = os.getenv("DB_USER", "cba_user")
    password: str = os.getenv("DB_PASSWORD", "cba_pass")
    raw_data_dir: str = os.getenv("RAW_DATA_DIR", "data/raw")

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

settings = Settings()
