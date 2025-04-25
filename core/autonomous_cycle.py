import os
from datetime import datetime
from core.conscious_memory import reflect_on_memory
from core.intent_mapper import detect_intention
from core.self_improvement_engine import run_self_improvement_cycle
from modules.auto_task_agent import run_task
from plugins.plugin_manager import auto_handle_file_or_text
from security.scanner import scan_target

JOURNAL_PATH = "data/memory/reflexion/jarvis_journal.md"

def get_todays_objective() -> str:
    """Extrait la dernière réflexion utile de Jarvis"""
    if not os.path.exists(JOURNAL_PATH):
        return None

    with open(JOURNAL_PATH, "r", encoding="utf-8") as f:
        lines = f.read().split("### ")
        if not lines:
            return None
        last = lines[-1]
        if "objectif" in last:
            return last.strip().split("objectif reste :")[-1].strip(". ").strip()
    return None

def generate_daily_plan(objective: str):
    """Planifie automatiquement les étapes du jour"""
    print(f"[Jarvis] Objectif du jour : {objective}")
    return run_task(f"Planifier la journée autour de cet objectif : {objective}")

def scan_env_for_inputs():
    """Simule la détection d’un fichier, d’un lien ou d’une idée à traiter"""
    test_inputs = [
        "https://example.com", 
        "data/raw/rapport.pdf", 
        "Prépare un résumé de mes dernières réflexions"
    ]

    results = []
    for i in test_inputs:
        intent = detect_intention(i)
        if intent["intention"] in ["chercher", "résumer", "analyser"]:
            result = auto_handle_file_or_text(i)
        elif intent["intention"] == "planifier":
            result = run_task(i)
        elif intent["intention"] == "analyser":
            result = scan_target(i)
        else:
            result = f"[Info] Intention détectée : {intent['intention']}, aucun module associé."
        results.append((i, result))
    return results

def run_autonomous_cycle():
    print("\n=== [ JARVIS - CYCLE AUTONOME ] ===\n")
    
    objective = get_todays_objective()
    if objective:
        print("[1] Objectif détecté →", objective)
        planning = generate_daily_plan(objective)
    else:
        print("[1] Aucun objectif trouvé dans la mémoire réflexive.")

    print("\n[2] Recherche de tâches ou actions à exécuter automatiquement…")
    actions = scan_env_for_inputs()
    for i, r in actions:
        print(f"\n→ Pour : {i}\n{r}")

    print("\n[3] Auto-amélioration…")
    patch = run_self_improvement_cycle()

    print(f"\n[✓] Jarvis autonome a terminé sa boucle. Patch : {patch}\n")

if __name__ == "__main__":
    run_autonomous_cycle()
