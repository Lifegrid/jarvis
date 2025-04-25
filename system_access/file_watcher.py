# system_access/file_watcher.py

import time
import os

def watch_folder(folder_path: str, interval: int = 5):
    print(f"👀 Surveillance du dossier : {folder_path}")
    before = set(os.listdir(folder_path))
    while True:
        time.sleep(interval)
        after = set(os.listdir(folder_path))
        added = after - before
        if added:
            print(f"🆕 Fichier détecté : {added}")
        before = after
