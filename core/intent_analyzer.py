def analyze_message(message: str) -> dict:
    """
    Détecte les intentions implicites dans un message utilisateur.
    Retourne un dictionnaire avec :
        - 'intent': nom de l’intention (str ou None)
        - 'action': commande système à exécuter (si applicable)
    """
    msg = message.lower()

    if "chrome" in msg or "navigateur" in msg or "internet" in msg:
        return {"intent": "open_browser", "action": "start chrome"}

    if "code" in msg or "vscode" in msg or "visual studio" in msg:
        return {"intent": "open_code_editor", "action": "code"}

    if "musique" in msg or "spotify" in msg or "écouter" in msg:
        return {"intent": "open_music", "action": "start spotify"}

    if "pause" in msg or "relax" in msg or "repos" in msg:
        return {"intent": "take_break", "action": None}

    if "mail" in msg or "email" in msg or "gmail" in msg:
        return {"intent": "open_mail", "action": "start outlook"}  # ou start chrome https://gmail.com

    if "fichier" in msg and "ouvrir" in msg:
        return {"intent": "open_file_explorer", "action": "start ."}

    # Ajoute ici tes propres règles personnalisées 👇
    if "chatgpt" in msg:
        return {"intent": "open_chatgpt", "action": "start chrome https://chat.openai.com"}

    return {"intent": None, "action": None}
