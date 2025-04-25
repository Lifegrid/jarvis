# 📁 memory_engine/memory_indexer.py
import os
import json
from datetime import datetime

MEMORY_PATH = "memory/snapshots.jsonl"

# Définitions simples de catégories de souvenirs
def categorize_memory(text):
    text = text.lower()
    if any(k in text for k in ["je m'appelle", "j'ai", "je suis né", "mon prénom", "travaille"]):
        return "profil"
    elif any(k in text for k in ["projet", "scraper", "euromillion", "ia personnelle"]):
        return "projet"
    elif any(k in text for k in ["chrome", "notepad", "fichier", "commande"]):
        return "système"
    elif any(k in text for k in ["crypto", "coinmarketcap", "finance"]):
        return "veille"
    return "général"


def store_memory_snapshot(text):
    category = categorize_memory(text)
    snapshot = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text,
        "category": category
    }
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    with open(MEMORY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(snapshot, ensure_ascii=False) + "\n")
    return snapshot


def load_snapshots(category_filter=None):
    if not os.path.exists(MEMORY_PATH):
        return []
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    snapshots = [json.loads(line) for line in lines]
    if category_filter:
        snapshots = [s for s in snapshots if s["category"] == category_filter]
    return snapshots
