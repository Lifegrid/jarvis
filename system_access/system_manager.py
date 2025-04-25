# system_access/system_manager.py

import os
import shutil

def create_file(path: str, content: str = ""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"📄 Fichier créé : {path}"

def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)
        return f"🗑️ Fichier supprimé : {path}"
    return f"❌ Fichier introuvable : {path}"

def move_file(src: str, dest: str):
    if os.path.exists(src):
        shutil.move(src, dest)
        return f"📦 Fichier déplacé de {src} → {dest}"
    return f"❌ Fichier source introuvable : {src}"
