import os
import json
import mimetypes
import importlib

PLUGIN_REGISTRY_PATH = "plugins/plugin.json"

def load_plugins():
    """Charge la liste des plugins enregistrés"""
    if os.path.exists(PLUGIN_REGISTRY_PATH):
        with open(PLUGIN_REGISTRY_PATH, "r") as f:
            return json.load(f)
    return []

plugins = load_plugins()

def handle_file(file_path: str) -> str:
    """Route un fichier uploadé vers le plugin approprié"""
    ext = os.path.splitext(file_path)[1].lower()
    matched_plugin = None

    for plugin in plugins:
        if plugin["input_type"] == "file" and ext in plugin.get("extensions", []):
            matched_plugin = plugin["name"]
            break

    if not matched_plugin:
        return f"[Alerte] Aucun plugin trouvé pour le type de fichier : {ext}"

    try:
        module = importlib.import_module(f"plugins.{matched_plugin}")
        return getattr(module, "process_file")(file_path)
    except Exception as e:
        return f"[Erreur] Impossible de traiter le fichier avec {matched_plugin} : {str(e)}"

def handle_message(message: str) -> str:
    """Route un message texte vers le plugin intelligent approprié"""
    triggers = {
        "email": "email_extractor",
        "planifie": "scheduler",
        "bilan": "smart_text_analyzer",
        "analyse": "smart_text_analyzer",
        "résume": "smart_text_analyzer",
        "rappelle-moi": "scheduler"
    }

    matched_plugin = None
    for keyword, plugin_name in triggers.items():
        if keyword.lower() in message.lower():
            matched_plugin = plugin_name
            break

    if not matched_plugin:
        # Sinon résumé intelligent par défaut
        matched_plugin = "smart_text_analyzer"

    try:
        module = importlib.import_module(f"plugins.{matched_plugin}")
        return getattr(module, "process_text")(message)
    except Exception as e:
        return f"[Erreur] Impossible de traiter le message avec {matched_plugin} : {str(e)}"
