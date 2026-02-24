from __future__ import annotations
import random
import string
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
from tqdm import tqdm

REGIONS = ["NA-West", "NA-East", "EU", "APAC"]
CHANNELS = ["organic", "paid_search", "email", "partner"]
PLANS = ["free", "pro", "team"]
DEVICES = ["web", "ios", "android"]
EVENT_TYPES = ["page_view", "click", "search", "feature_use", "purchase"]
FEATURES = ["onboarding", "search", "export", "collaboration", "settings", "billing"]

def _rand_id(prefix: str, n: int = 12) -> str:
    return prefix + "".join(random.choices(string.ascii_lowercase + string.digits, k=n))

def generate_synthetic_data(out_dir: str, rows: int = 100_000, seed: int = 42) -> None:
    random.seed(seed)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    user_count = max(5000, rows // 50)
    start = datetime.utcnow() - timedelta(days=120)

    users = []
    for _ in range(user_count):
        signup = start + timedelta(days=random.randint(0, 90), hours=random.randint(0, 23))
        users.append({
            "user_id": _rand_id("u_"),
            "signup_ts": signup.isoformat(sep=" ", timespec="seconds"),
            "region": random.choice(REGIONS),
            "channel": random.choice(CHANNELS),
            "plan": random.choice(PLANS),
        })
    users_df = pd.DataFrame(users)
    users_path = out / "users.csv"
    users_df.to_csv(users_path, index=False)

    user_ids = users_df["user_id"].tolist()
    events = []
    for _ in tqdm(range(rows), desc="Generating events"):
        user_id = random.choice(user_ids)
        session_id = _rand_id("s_")
        base_ts = start + timedelta(days=random.randint(0, 119), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        events_in_session = random.randint(1, 12)
        device = random.choice(DEVICES)
        for i in range(events_in_session):
            if len(events) >= rows:
                break
            event_ts = base_ts + timedelta(minutes=i * random.randint(1, 4))
            event_type = random.choices(EVENT_TYPES, weights=[55, 20, 10, 12, 3], k=1)[0]
            feature = None
            amount = None
            if event_type in ("feature_use", "purchase"):
                feature = random.choice(FEATURES)
            if event_type == "purchase":
                amount = round(random.uniform(5, 250), 2)
            events.append({
                "event_id": _rand_id("e_"),
                "user_id": user_id,
                "session_id": session_id,
                "event_ts": event_ts.isoformat(sep=" ", timespec="seconds"),
                "event_type": event_type,
                "feature": feature,
                "device": device,
                "amount": amount,
            })

    events_df = pd.DataFrame(events[:rows])
    events_path = out / "events.csv"
    events_df.to_csv(events_path, index=False)
