# code_executor/code_executor.py

import subprocess
import tempfile
import os
import sys

def run_python_code(code: str) -> dict:
    """
    Exécute du code Python de manière isolée et renvoie le résultat.
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as temp:

        temp.write(code)
        temp.flush()
        temp_path = temp.name

    try:
        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        return {
            "status": "success" if result.returncode == 0 else "error",
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }

    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "stderr": "⏱️ Temps d'exécution dépassé.",
            "stdout": "",
            "returncode": -1
        }

    finally:
        os.unlink(temp_path)
