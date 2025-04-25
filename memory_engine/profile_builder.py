import json
import os
import re
from datetime import datetime

PROFILE_PATH = "memory_engine/user_profile.json"

def load_profile():
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_profile(profile):
    with open(PROFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)

def update_user_profile(user_input):
    profile = load_profile()

    # Analyse simple et améliorée
    if "je m'appelle" in user_input.lower():
        match = re.search(r"(je m'appelle|je suis)\s+([A-Za-zÀ-ÿ-]+)", user_input, re.IGNORECASE)
        if match:
            profile["prénom"] = match.group(2)

    if "j'ai" in user_input.lower() and "ans" in user_input.lower():
        match = re.search(r"j'ai\s+(\d+)\s+ans", user_input, re.IGNORECASE)
        if match:
            profile["âge"] = match.group(1)

    if "je suis né" in user_input.lower():
        match = re.search(r"je suis né[ée]?\s+(en\s+)?(\d{4})", user_input, re.IGNORECASE)
        if match:
            profile["année_de_naissance"] = match.group(2)

    if "je travaille" in user_input.lower() or "je bosse" in user_input.lower():
        match = re.search(r"je (travaille|bosse)[\w\s]*?\s+au\s+([\w\s\-']+)", user_input, re.IGNORECASE)
        if match:
            profile["travail"] = f"au {match.group(2)}"

    if "je suis passionné" in user_input.lower():
        match = re.search(r"je suis passionné par\s+([\w\s,]+)", user_input, re.IGNORECASE)
        if match:
            profile["passions"] = match.group(1)

    if "je veux" in user_input.lower():
        match = re.search(r"je veux\s+(.*)", user_input, re.IGNORECASE)
        if match:
            profile["objectif"] = match.group(1)

    save_profile(profile)

def get_user_profile():
    profile = load_profile()
    return json.dumps(profile, indent=2, ensure_ascii=False)
