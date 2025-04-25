import os
import json

def load_profile(path="profile.json") -> dict:
    if not os.path.exists(path):
        return {
            "name": "Jérémie",
            "interests": ["tech", "IA", "crypto"],
            "routines": ["bilan quotidien", "veille techno"]
        }
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
