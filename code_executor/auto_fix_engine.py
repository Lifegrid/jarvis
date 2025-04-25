import subprocess
import tempfile
import os
from core_llm.llm_client import chat_with_llm


def execute_python_code(file_path):
    try:
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), 1


def auto_fix_and_run(code, max_attempts=3):
    attempt = 1
    last_error = ""
    current_code = code

    while attempt <= max_attempts:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as tmp:
            tmp.write(current_code)
            tmp_path = tmp.name

        stdout, stderr, returncode = execute_python_code(tmp_path)

        if returncode == 0:
            os.unlink(tmp_path)
            return {
                "success": True,
                "output": stdout,
                "error": None,
                "attempts": attempt,
                "corrected_code": current_code
            }
        else:
            print(f"⚠️ Erreur détectée à l'exécution (tentative {attempt}) :\n{stderr}")
            last_error = stderr
            try:
                prompt = f"Corrige ce code Python qui échoue à cause de cette erreur :\nErreur : {stderr}\n\nCode :\n{current_code}"
                current_code = chat_with_llm(prompt)
                attempt += 1
            except Exception as e:
                return {
                    "success": False,
                    "output": stdout,
                    "error": f"Erreur pendant la correction : {e}",
                    "attempts": attempt - 1,
                    "corrected_code": current_code
                }

    return {
        "success": False,
        "output": stdout,
        "error": last_error,
        "attempts": attempt - 1,
        "corrected_code": current_code
    }
