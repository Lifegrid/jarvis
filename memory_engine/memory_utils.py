import os
import json
import re
from datetime import datetime

MEMORY_PATH = "memories"

def sanitize_filename(text: str) -> str:
    """Nettoie et raccourcit un nom de fichier"""
    if not isinstance(text, str):
        text = str(text)
    text = re.sub(r'[^\w\s-]', '', text).strip().replace(' ', '_')
    return text[:50]

def store_memory_snapshot(category: str, content):
    """Stocke une mémoire dans un fichier JSON avec nom sûr"""

    if not os.path.exists(MEMORY_PATH):
        os.makedirs(MEMORY_PATH)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if isinstance(content, dict):
        preview = content.get("user") or content.get("text") or json.dumps(content)
    elif isinstance(content, str):
        preview = content
    else:
        preview = str(content)

    safe_name = sanitize_filename(preview or "memoire")
    filename = os.path.join(MEMORY_PATH, f"{safe_name}_{timestamp}.json")

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
    except OSError as e:
        fallback = f"memory_{timestamp}.json"
        with open(os.path.join(MEMORY_PATH, fallback), "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
