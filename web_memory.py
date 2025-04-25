import os
import json
from datetime import datetime, timedelta

WEB_MEMORY_PATH = "web_memory_store.json"

def _load_memory():
    if os.path.exists(WEB_MEMORY_PATH):
        with open(WEB_MEMORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def _save_memory(memory):
    with open(WEB_MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def store_web_memory(query: str, result: str):
    memory = _load_memory()
    memory.append({
        "query": query,
        "result": result,
        "timestamp": datetime.now().isoformat()
    })
    _save_memory(memory)

def get_web_memory():
    return _load_memory()

def get_recent_web_memories(hours: int = 24):
    memory = _load_memory()
    cutoff = datetime.now() - timedelta(hours=hours)
    recent = [m for m in memory if datetime.fromisoformat(m["timestamp"]) > cutoff]
    return recent

def find_similar_query(query: str) -> str | None:
    memory = _load_memory()
    query_lower = query.lower()
    for m in reversed(memory):
        if query_lower in m["query"].lower() or m["query"].lower() in query_lower:
            return m["result"]
    return None
