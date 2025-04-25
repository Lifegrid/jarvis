import os
import webbrowser
import subprocess

def detect_intent_and_execute(text: str) -> str:
    """Détecte une intention dans une phrase et exécute une action système associée."""
    lower = text.lower()

    # Ouvrir Visual Studio Code
    if "visual studio code" in lower or "vscode" in lower:
        os.system("code .")
        return "✅ J'ai ouvert Visual Studio Code."

    # Ouvrir un terminal
    elif "terminal" in lower or "invite de commande" in lower:
        os.system("start cmd")
        return "✅ Terminal ouvert."

    # Afficher les fichiers dans Documents
    elif "dossier documents" in lower:
        path = os.path.join(os.path.expanduser("~"), "Documents")
        os.startfile(path)
        return f"📂 J'ai ouvert ton dossier Documents."

    # Ouvrir un site web
    elif "ouvre" in lower and "http" in lower:
        url = lower.split("ouvre")[-1].strip()
        if not url.startswith("http"):
            url = "http://" + url
        webbrowser.open(url)
        return f"🌐 J'ai ouvert le site {url}"

    # Éteindre l'ordinateur (exemple, à confirmer)
    elif "éteins l'ordinateur" in lower or "shutdown" in lower:
        return "⚠️ Tu veux vraiment que j’éteigne le PC ? Cette commande est désactivée pour le moment."

    return "❌ Je n'ai pas détecté d'action système claire dans ta phrase."
