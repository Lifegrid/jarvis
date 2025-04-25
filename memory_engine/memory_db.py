import json
import os
from datetime import datetime

MEMORY_FILE = "memory_engine/long_term_memory.json"

def store_web_insight(query: str, links: list[str], summary: str):
    memory = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)

    memory.append({
        "type": "web_research",
        "query": query,
        "summary": summary,
        "links": links,
        "timestamp": datetime.now().isoformat()
    })

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def get_all_memories() -> list:
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

