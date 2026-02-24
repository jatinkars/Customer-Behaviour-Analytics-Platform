DROP TABLE IF EXISTS analytics.fact_session;
CREATE TABLE analytics.fact_session AS
SELECT
  e.session_id,
  e.user_id,
  MIN(e.event_ts) AS session_start_ts,
  MAX(e.event_ts) AS session_end_ts,
  COUNT(*)        AS events_in_session,
  SUM(CASE WHEN e.event_type = 'purchase' THEN COALESCE(e.amount,0) ELSE 0 END) AS purchase_amount,
  MAX(e.device)   AS device
FROM staging.events e
GROUP BY 1,2;

CREATE INDEX IF NOT EXISTS idx_fact_session_user ON analytics.fact_session(user_id);

DROP TABLE IF EXISTS analytics.fact_user_daily;
CREATE TABLE analytics.fact_user_daily AS
SELECT
  u.user_id,
  DATE(e.event_ts) AS activity_date,
  COUNT(*)         AS events,
  COUNT(DISTINCT e.session_id) AS sessions,
  SUM(CASE WHEN e.event_type = 'purchase' THEN COALESCE(e.amount,0) ELSE 0 END) AS revenue
FROM staging.users u
JOIN staging.events e ON u.user_id = e.user_id
GROUP BY 1,2;

CREATE INDEX IF NOT EXISTS idx_fact_user_daily_date ON analytics.fact_user_daily(activity_date);

DROP TABLE IF EXISTS analytics.cohort_retention_weekly;
CREATE TABLE analytics.cohort_retention_weekly AS
WITH cohort AS (
  SELECT
    user_id,
    DATE_TRUNC('week', signup_ts)::DATE AS cohort_week
  FROM staging.users
),
activity AS (
  SELECT
    user_id,
    DATE_TRUNC('week', event_ts)::DATE AS activity_week
  FROM staging.events
  GROUP BY 1,2
),
joined AS (
  SELECT
    c.cohort_week,
    a.activity_week,
    (a.activity_week - c.cohort_week) / 7 AS weeks_since_signup,
    COUNT(DISTINCT a.user_id) AS active_users
  FROM cohort c
  JOIN activity a ON a.user_id = c.user_id
  WHERE a.activity_week >= c.cohort_week
  GROUP BY 1,2,3
),
cohort_size AS (
  SELECT cohort_week, COUNT(DISTINCT user_id) AS cohort_users
  FROM cohort
  GROUP BY 1
)
SELECT
  j.cohort_week,
  j.activity_week,
  j.weeks_since_signup,
  cs.cohort_users,
  j.active_users,
  (j.active_users::NUMERIC / NULLIF(cs.cohort_users,0)) AS retention_rate
FROM joined j
JOIN cohort_size cs USING (cohort_week);

CREATE INDEX IF NOT EXISTS idx_cohort_retention_week ON analytics.cohort_retention_weekly(cohort_week);
