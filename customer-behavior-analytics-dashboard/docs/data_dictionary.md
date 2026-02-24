# Data Dictionary

## staging.users
- `user_id` (TEXT, PK): unique user identifier
- `signup_ts` (TIMESTAMP): signup timestamp
- `region` (TEXT): region segment
- `channel` (TEXT): acquisition channel
- `plan` (TEXT): plan tier

## staging.events
- `event_id` (TEXT, PK): unique event identifier
- `user_id` (TEXT, FK): user identifier
- `session_id` (TEXT): session identifier
- `event_ts` (TIMESTAMP): event timestamp
- `event_type` (TEXT): page_view/click/search/feature_use/purchase
- `feature` (TEXT): feature name (if feature_use/purchase)
- `device` (TEXT): web/ios/android
- `amount` (NUMERIC): purchase amount (if purchase)

## analytics.fact_session
Session-level aggregation:
- session start/end
- events per session
- purchase amount per session

## analytics.fact_user_daily
User-day aggregation:
- sessions
- events
- revenue

## analytics.cohort_retention_weekly
Cohort retention table:
- cohort_week (DATE)
- activity_week (DATE)
- weeks_since_signup (INT)
- cohort_users (INT)
- active_users (INT)
- retention_rate (NUMERIC)

## analytics.vw_kpis_daily
Daily KPI view:
- DAU
- sessions
- sessions per user
- revenue
