# system_access/app_launcher.py

import subprocess
import os

def launch_app(app_name: str):
    known_apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad.exe",
        "explorer": "explorer.exe"
    }

    app_key = app_name.lower().strip().replace("ouvrir", "").replace("lancer", "").replace(" ", "")
    for key, path in known_apps.items():
        if key in app_key:
            try:
                subprocess.Popen(path)
                return path
            except Exception as e:
                return f"Erreur de lancement : {str(e)}"
    return f"❌ Application inconnue : {app_name}"

def install_app(app_id: str):
    try:
        result = subprocess.run(
            ["winget", "install", "--id", app_id, "-e", "--source", "msstore"],
            capture_output=True, text=True
        )
        return result.stdout + result.stderr
    except Exception as e:
        return f"Erreur pendant l'installation : {str(e)}"
