LEARNING_FILE = "memory_engine/learning_log.txt"

def log_learning(insight: str):
    with open(LEARNING_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n🧠 Apprentissage: {insight}\n")