import subprocess
import tempfile

def execute_python_code(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode='w', encoding='utf-8') as temp:
        temp.write(code)
        temp.flush()
        result = subprocess.run(
            ["python", temp.name],
            capture_output=True,
            text=True
        )

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    return_code = result.returncode

    return {
        "stdout": stdout,
        "stderr": stderr,
        "return_code": return_code
    }
