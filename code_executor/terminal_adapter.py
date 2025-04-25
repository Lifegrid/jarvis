# code_executor/terminal_adapter.py

import subprocess

def run_command(command: str, shell: str = "powershell") -> dict:
    """
    Exécute une commande dans PowerShell (ou Bash si Linux/Mac).
    """
    if shell == "powershell":
        shell_cmd = ["powershell", "-Command", command]
    elif shell == "cmd":
        shell_cmd = ["cmd", "/c", command]
    else:
        shell_cmd = [shell, "-c", command]

    try:
        result = subprocess.run(
            shell_cmd,
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
            "stdout": "",
            "stderr": "⏱️ Temps d'exécution dépassé.",
            "returncode": -1
        }
