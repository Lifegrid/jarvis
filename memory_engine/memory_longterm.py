import json, os

MEMORY_FILE = "memory_engine/longterm_memory.json"

def save_fact(fact: str):
    data = load_memory()
    data.append(fact)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search_memory(keyword: str) -> list[str]:
    return [m for m in load_memory() if keyword.lower() in m.lower()]