# Customer Behavior Analytics Dashboard (SQL • Python • Tableau)

End-to-end analytics project for **user engagement, cohort retention, and behavioral trends**.

**What this repo includes**
- Synthetic dataset generator (scale to **500K+ events**)
- Postgres schema + SQL marts (cohort retention, sessions, daily user metrics)
- Python ETL to load raw data → build analytics tables/views
- Tableau build spec (worksheets, calculated fields, filters, parameters)
- Example “insight memo” with actionable recommendations

> Note: This repo ships with **synthetic data** so anyone can run it locally.

---

## Project Overview

**Goal:** Enable stakeholders to explore engagement and retention quickly via a Tableau dashboard backed by clean SQL marts.

**Core outputs**
- **Retention trends** (cohort-based, week-over-week)
- **Usage cohorts** (signup cohort vs activity)
- **Engagement patterns** (sessions, events, feature usage)
- **Segment analysis** (channel, region, plan, device)

---

## Tech Stack
- **Database:** Postgres (Docker Compose)
- **SQL:** schema, marts, cohort retention logic
- **Python:** pandas + SQLAlchemy ETL
- **Tableau:** dashboard consuming analytics tables/views

---

## Quickstart (Local)

### 1) Start Postgres
```bash
docker compose up -d
```

### 2) Create a virtual environment + install deps
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3) Configure environment
Copy `.env.example` → `.env` and edit if needed.

### 4) Generate synthetic data (default: 100k events)
```bash
python -m src.cli generate-data --rows 100000
```

### 5) Load + build analytics marts
```bash
python -m src.cli init-db
python -m src.cli load-raw
python -m src.cli build-marts
```

### 6) Connect Tableau
- Connect to Postgres using the credentials in `.env`
- Use tables/views in schema: `analytics`
- Follow: `tableau/tableau_dashboard_spec.md`

---

## Repo Structure
```
.
├── data/
│   ├── raw/                # generated CSVs (gitignored)
│   └── samples/            # tiny sample CSVs committed for quick demo
├── docker-compose.yml
├── sql/
│   ├── 01_schema.sql
│   ├── 02_staging.sql
│   ├── 03_marts.sql
│   └── 04_views.sql
├── src/
│   ├── cli.py
│   ├── utils/
│   ├── etl/
│   └── metrics/
├── tableau/
│   ├── tableau_dashboard_spec.md
│   └── tableau_calculated_fields.md
└── docs/
    ├── data_dictionary.md
    └── recommendations.md
```

---

## Key Metrics
- DAU / WAU / MAU
- Sessions per user
- Events per session
- Retention rate by cohort week
- Feature usage distribution
- Segment performance (channel, region, plan)

---

## Common Commands
```bash
python -m src.cli --help
python -m src.cli generate-data --rows 500000
python -m src.cli rebuild-all --rows 500000
```

---

## How to publish to GitHub
```bash
git init
git add .
git commit -m "Initial commit: customer behavior analytics dashboard"
git branch -M main
git remote add origin https://github.com/<your-username>/customer-behavior-analytics-dashboard.git
git push -u origin main
```
