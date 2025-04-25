from web.web_research import autonomous_web_research
from web.web_memory import store_web_summary

def run_objective(goal: str) -> str:
    """Exécute un objectif donné, type : Trouve une solution, compare, résume."""
    result = autonomous_web_research(goal)
    store_web_summary(goal, result)
    return f"📌 Objectif : {goal}\n\n{result}"