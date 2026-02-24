from __future__ import annotations
import argparse
from .utils.db import get_engine
from .utils.config import settings
from .etl.generate_data import generate_synthetic_data
from .etl.init_db import init_db
from .etl.load_raw import load_raw
from .etl.build_marts import build_marts

def main():
    parser = argparse.ArgumentParser(prog="cba", description="Customer Behavior Analytics (SQL • Python • Tableau)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_gen = sub.add_parser("generate-data", help="Generate synthetic raw CSVs")
    p_gen.add_argument("--rows", type=int, default=100_000, help="Number of events rows (default: 100k)")

    sub.add_parser("init-db", help="Create schemas and staging tables")
    sub.add_parser("load-raw", help="Load raw CSVs into staging tables")
    sub.add_parser("build-marts", help="Build analytics marts and views")

    p_rebuild = sub.add_parser("rebuild-all", help="Generate data + init db + load + build marts")
    p_rebuild.add_argument("--rows", type=int, default=100_000)

    args = parser.parse_args()
    engine = get_engine()

    if args.cmd == "generate-data":
        generate_synthetic_data(settings.raw_data_dir, rows=args.rows)
    elif args.cmd == "init-db":
        init_db(engine)
    elif args.cmd == "load-raw":
        load_raw(engine)
    elif args.cmd == "build-marts":
        build_marts(engine)
    elif args.cmd == "rebuild-all":
        generate_synthetic_data(settings.raw_data_dir, rows=args.rows)
        init_db(engine)
        load_raw(engine)
        build_marts(engine)

if __name__ == "__main__":
    main()
