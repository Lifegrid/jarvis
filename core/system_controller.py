import os
import platform
import subprocess

APPS = {
    "chrome": {
        "Windows": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "Darwin": "/Applications/Google Chrome.app",
        "Linux": "google-chrome"
    },
    "vscode": {
        "Windows": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "Darwin": "/Applications/Visual Studio Code.app",
        "Linux": "code"
    },
    "discord": {
        "Windows": r"C:\Users\%USERNAME%\AppData\Local\Discord\Update.exe",
        "Darwin": "/Applications/Discord.app",
        "Linux": "discord"
    }
}

def open_application(name: str) -> str:
    system = platform.system()
    path = APPS.get(name.lower(), {}).get(system)
    
    if not path:
        return f"[Erreur] Application inconnue ou non définie pour {system}."

    try:
        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin":
            subprocess.Popen(["open", path])
        elif system == "Linux":
            subprocess.Popen([path])
        return f"[Jarvis] Application '{name}' lancée avec succès."
    except Exception as e:
        return f"[Erreur lancement {name}] {str(e)}"

def execute_command(cmd: str) -> str:
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=8)
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        return f"[Erreur exécution] {e.output.decode('utf-8').strip()}"
    except Exception as e:
        return f"[Erreur terminal] {str(e)}"

def create_file(path: str, content: str = "") -> str:
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"[Jarvis] Fichier créé : {path}"
    except Exception as e:
        return f"[Erreur création fichier] {str(e)}"

# Test CLI
if __name__ == "__main__":
    print(open_application("chrome"))
    print(execute_command("echo Hello depuis Jarvis"))
    print(create_file("data/tmp/test.txt", "Jarvis écrit ce fichier."))
