# memory_engine/active_memory.py

import json
import os
from datetime import datetime

MEMORY_PATH = "memory_engine/active_memory.json"
SNAPSHOT_PATH = "memory_engine/memory_snapshots.json"

def store_memory_snapshot(entry, label="interaction"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    snapshot = {"timestamp": timestamp, "label": label, "content": entry}

    data = []
    if os.path.exists(SNAPSHOT_PATH):
        with open(SNAPSHOT_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass

    data.append(snapshot)
    with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_memory_snapshots(limit=None):
    if not os.path.exists(SNAPSHOT_PATH):
        return []
    with open(SNAPSHOT_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data[-limit:] if limit else data
        except json.JSONDecodeError:
            return []
