import datetime
from core.llm_interface import call_llm  # Appelle ton LLM local
from core.intent_mapper import detect_intention
from modules.web_research import summarize_url_if_detected  # exemple d'étape réutilisable

REPORTS_PATH = "data/summaries/"

def decompose_task(goal: str) -> list:
    """Décompose une mission en étapes grâce à l'IA"""
    system_prompt = (
        "Tu es un assistant intelligent. Décompose la mission suivante en 3 à 7 étapes pratiques "
        "que tu peux exécuter ou simuler seul. Donne uniquement la liste sans explication."
    )
    response = call_llm(goal, system_prompt)
    return [step.strip("-• ") for step in response.split("\n") if step.strip()]

def execute_step(step: str) -> str:
    """Tente d'exécuter une étape (ou la simule si non codée)"""
    intent = detect_intention(step)["intention"]
    
    if intent == "chercher":
        return summarize_url_if_detected(step)
    elif intent == "résumer":
        return "[Simulation] Résumé du contenu demandé."
    elif intent == "planifier":
        return "[Simulation] Tâche planifiée dans l'agenda."
    elif intent == "coder":
        return "[Simulation] Génération d’un script."
    else:
        return f"[Simulation] Étape '{step}' interprétée comme intention : {intent}."

def generate_task_report(goal: str, steps: list, results: list) -> str:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    report = f"# Rapport de mission – {goal}\nDate : {now}\n\n"
    for i, (step, result) in enumerate(zip(steps, results)):
        report += f"## Étape {i+1} : {step}\nRésultat : {result}\n\n"
    return report

def save_task_report(content: str, goal: str) -> str:
    filename = REPORTS_PATH + "task_" + goal.replace(" ", "_")[:30] + ".md"
    with open(filename, "w") as f:
        f.write(content)
    return filename

def run_task(goal: str) -> str:
    print(f"[Jarvis] Mission reçue : {goal}")
    steps = decompose_task(goal)
    results = [execute_step(step) for step in steps]
    report = generate_task_report(goal, steps, results)
    path = save_task_report(report, goal)
    print(f"[Jarvis] Rapport généré dans : {path}")
    return path

if __name__ == "__main__":
    goal = "Créer un plan d’action pour un site web personnel"
    run_task(goal)
