import json
from datetime import datetime

def log_usage(username: str, location: str):
    entry = {
        "user": username,
        "location": location,
        "timestamp": datetime.now().isoformat()
    }
    try:
        with open("usage/usage_log.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)
    with open("usage/usage_log.json", "w") as f:
        json.dump(data, f, indent=2)
