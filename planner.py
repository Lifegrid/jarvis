import datetime

routine = [
    {"time": "08:00", "task": "Réveil, café et planification"},
    {"time": "09:00", "task": "Lancement travail important"},
    {"time": "12:00", "task": "Pause et repas"},
    {"time": "14:00", "task": "Deep Work"},
    {"time": "17:00", "task": "Clôture, sauvegarde, journal"},
]

def get_next_task():
    now = datetime.datetime.now().strftime("%H:%M")
    for item in routine:
        if now <= item["time"]:
            return item["task"]
    return "Fin de journée, détente."
