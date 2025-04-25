import json
import os

PROFILE_PATH = "config/user_profile.json"

def get_user_profile():
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def update_user_profile(new_data: dict):
    profile = get_user_profile()
    profile.update(new_data)
    with open(PROFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4, ensure_ascii=False)

def generate_profile_prompt():
    profile = get_user_profile()
    if not profile:
        return ""
    
    name = profile.get("name", "Utilisateur")
    job = profile.get("job", "")
    location = profile.get("location", "")
    passion = profile.get("passion", "")
    
    return (f"Tu t'appelles {name}, tu travailles {job}, "
            f"tu es passionné par {passion}. "
            f"Tu veux que je t’aide à organiser ta journée ou à scraper des actus crypto ? 😉")
