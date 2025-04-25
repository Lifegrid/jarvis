# 📁 Fichier : system_access/file_search.py

import os

def search_files(root_dir, keyword):
    results = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if keyword.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

def list_directory(path):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        return f"❌ Dossier introuvable : {path}"
    except Exception as e:
        return f"❌ Erreur : {str(e)}"

def file_exists(path):
    return os.path.exists(path)

def get_absolute_path(relative_path):
    return os.path.abspath(relative_path)
