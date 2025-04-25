import subprocess
import platform

def execute_action(command: str) -> str:
    """
    Exécute une commande système en toute sécurité.
    Compatible Windows (par défaut) — Linux/Mac à adapter.
    Retourne une réponse texte.
    """
    try:
        system = platform.system()

        if system == "Windows":
            subprocess.Popen(command, shell=True)
        elif system == "Darwin":
            subprocess.Popen(["open", command])
        elif system == "Linux":
            subprocess.Popen(["xdg-open", command])
        else:
            return "❌ Système d'exploitation non supporté."

        return f"✅ Action exécutée : `{command}`"

    except Exception as e:
        return f"❌ Erreur d'exécution : {str(e)}"