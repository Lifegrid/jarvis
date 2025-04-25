# autonomy/autonomous_executor.py

from autonomy.action_planner import generate_action_plan
from autonomy.autonomy_logger import log_autonomy_event
from autonomy.opportunity_detector import detect_opportunities
from core_llm.llm_client import chat_with_llm
from code_executor.code_engine import execute_python_code
from code_executor.code_writer import write_code_to_file


def run_autonomous_cycle(profile):
    print("\n🧠 [Autonomie] Lancement du cycle autonome...")

    opportunities = detect_opportunities(profile)
    if not opportunities:
        print("🤖 Aucune opportunité détectée.")
        return

    for opportunity in opportunities:
        log_autonomy_event("Opportunité détectée", opportunity)

        plan = generate_action_plan(opportunity)
        log_autonomy_event("Plan d'action généré", plan)

        if "code" in plan:
            print("🧾 Génération de code...")
            code = chat_with_llm(plan["code"])
            filename = write_code_to_file(code)
            output, error = execute_python_code(filename)
            log_autonomy_event("Code exécuté", {"output": output, "error": error})
            print("✅ Code exécuté.\n📄 Résultat :", output, "\n❗ Erreurs :", error or "aucune")

        elif "instruction" in plan:
            print("🧭 Instruction autonome :", plan["instruction"])
            log_autonomy_event("Instruction exécutée", plan["instruction"])

    print("✅ [Autonomie] Cycle terminé.")
