CREATE OR REPLACE VIEW analytics.vw_kpis_daily AS
WITH dau AS (
  SELECT activity_date, COUNT(DISTINCT user_id) AS dau
  FROM analytics.fact_user_daily
  GROUP BY 1
),
sessions AS (
  SELECT activity_date, SUM(sessions) AS sessions
  FROM analytics.fact_user_daily
  GROUP BY 1
),
revenue AS (
  SELECT activity_date, SUM(revenue) AS revenue
  FROM analytics.fact_user_daily
  GROUP BY 1
)
SELECT
  d.activity_date,
  d.dau,
  s.sessions,
  (s.sessions::NUMERIC / NULLIF(d.dau,0)) AS sessions_per_user,
  r.revenue
FROM dau d
JOIN sessions s USING (activity_date)
JOIN revenue r USING (activity_date)
ORDER BY 1;
