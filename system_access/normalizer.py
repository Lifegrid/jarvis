# 📁 system_access/normalizer.py

def normalize_app_name(user_input: str) -> str:
    user_input = user_input.lower()
    if "chrome" in user_input:
        return "chrome"
    if "bloc" in user_input or "notepad" in user_input:
        return "notepad"
    if "explorateur" in user_input or "explorer" in user_input:
        return "explorer"
    return user_input.strip()


def normalize_file_command(user_input: str) -> str:
    if "mes documents" in user_input.lower() or "fichiers" in user_input.lower():
        return "list_files"
    return "chat"
