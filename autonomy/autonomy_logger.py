# autonomy/autonomy_logger.py

import os
from datetime import datetime

LOG_FILE = "logs/autonomy.log"

def log_autonomy_event(action: str, result: str = ""):
    """
    Enregistre une action autonome avec un timestamp.
    """
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] ACTION: {action} | RESULT: {result}\n")
