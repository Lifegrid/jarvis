# system_access/app_installer.py

import subprocess

def install_app(app_name: str):
    try:
        command = f"winget install --silent --accept-package-agreements --accept-source-agreements {app_name}"
        subprocess.run(command, shell=True)
        return f"📦 Installation en cours : {app_name}"
    except Exception as e:
        return f"❌ Erreur installation : {e}"
