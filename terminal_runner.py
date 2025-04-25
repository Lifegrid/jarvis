import subprocess
import os
from typing import Literal

ALLOWED_COMMANDS = [
    "ls", "dir", "python", "node", "npm", "npx", "echo", "cd", "type", "cat"
]

BLOCKED_KEYWORDS = ["rm", "del", "shutdown", "reboot", "format", ":\\"]


def is_command_safe(command: str) -> bool:
    return any(command.startswith(cmd) for cmd in ALLOWED_COMMANDS) and not any(bad in command for bad in BLOCKED_KEYWORDS)


def run_shell_command(command: str, shell: Literal["bash", "powershell"] = "bash") -> dict:
    if not is_command_safe(command):
        return {"error": "Commande non autorisée pour des raisons de sécurité."}

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            executable="/bin/bash" if shell == "bash" else None
        )
        return {
            "success": True,
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }
    except Exception as e:
        return {"error": str(e)}


