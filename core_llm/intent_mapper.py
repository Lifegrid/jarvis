# core_llm/intent_mapper.py

def map_intent(text: str) -> str:
    lowered = text.lower()

    if "installe" in lowered:
        return "install_app"
    elif "déplace" in lowered:
        return "move_file"
    elif "supprime" in lowered:
        return "delete_file"
    elif "crée" in lowered and "fichier" in lowered:
        return "create_file"
    elif "ouvre" in lowered or "lance" in lowered:
        return "launch_app"
    elif "plugin" in lowered:
        return "plugin"
    elif ("code" in lowered or "script" in lowered or "python" in lowered):
        if "exécute" in lowered or "puis" in lowered:
            return "generate_and_run_code"
        return "code_exec"
    else:
        return "chat"
