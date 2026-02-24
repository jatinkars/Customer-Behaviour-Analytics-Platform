# Tableau Dashboard Spec

Connect Tableau to Postgres and use schema `analytics`.

## Recommended Data Sources
- `analytics.cohort_retention_weekly`
- `analytics.fact_user_daily`
- `analytics.vw_kpis_daily`
- (optional) `analytics.fact_session`

## Dashboard Pages / Worksheets

### 1) Executive Overview
- KPI tiles: DAU, Sessions, Sessions/User, Revenue (from `vw_kpis_daily`)
- Trend lines for DAU and Sessions

### 2) Cohort Retention
- Heatmap: `cohort_week` (rows) vs `weeks_since_signup` (columns)
- Color: `retention_rate`
- Tooltip: cohort_users, active_users, retention_rate

### 3) Engagement by Segment
- Filters: `region`, `channel`, `plan`
- Bar chart: Sessions/User by segment
- Line chart: DAU trend by segment (optional blend or separate view)

### 4) Feature Usage (Optional if you extend marts)
- If you add a feature mart, show % of users using a feature per week

## Recommended Filters / Parameters
- Date Range (for KPIs)
- Cohort Range (cohort_week)
- Segment filters (region/channel/plan)
- Parameter: max weeks since signup displayed (e.g., 0–12)
