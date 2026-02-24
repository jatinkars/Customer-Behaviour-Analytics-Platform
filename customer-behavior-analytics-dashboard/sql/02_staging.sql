DROP TABLE IF EXISTS staging.users;
CREATE TABLE staging.users (
  user_id           TEXT PRIMARY KEY,
  signup_ts         TIMESTAMP NOT NULL,
  region            TEXT,
  channel           TEXT,
  plan              TEXT
);

DROP TABLE IF EXISTS staging.events;
CREATE TABLE staging.events (
  event_id          TEXT PRIMARY KEY,
  user_id           TEXT NOT NULL,
  session_id        TEXT NOT NULL,
  event_ts          TIMESTAMP NOT NULL,
  event_type        TEXT NOT NULL,
  feature           TEXT,
  device            TEXT,
  amount            NUMERIC,
  FOREIGN KEY (user_id) REFERENCES staging.users(user_id)
);

CREATE INDEX IF NOT EXISTS idx_events_user_ts ON staging.events(user_id, event_ts);
CREATE INDEX IF NOT EXISTS idx_events_session ON staging.events(session_id);
