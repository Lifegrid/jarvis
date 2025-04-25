import requests
import socket
from urllib.parse import urlparse

def basic_host_info(target: str):
    """Analyse un domaine ou une IP et retourne infos de base"""
    info = {"target": target}

    try:
        parsed = urlparse(target)
        hostname = parsed.hostname or target
        ip = socket.gethostbyname(hostname)
        info["hostname"] = hostname
        info["ip"] = ip
    except Exception as e:
        info["error"] = f"DNS lookup failed: {e}"
        return info

    try:
        response = requests.get(target, timeout=5)
        headers = dict(response.headers)

        info["status_code"] = response.status_code
        info["headers"] = headers
        info["server"] = headers.get("Server", "Inconnu")
        info["powered_by"] = headers.get("X-Powered-By", "Non spécifié")
        info["content_type"] = headers.get("Content-Type", "")
    except Exception as e:
        info["error"] = f"Connection failed: {e}"

    return info

def format_report(scan_result: dict) -> str:
    if "error" in scan_result:
        return f"# Échec du scan\nErreur : {scan_result['error']}"

    lines = [
        f"# Analyse de surface de {scan_result['target']}",
        f"- IP : {scan_result['ip']}",
        f"- Code HTTP : {scan_result.get('status_code', 'N/A')}",
        f"- Serveur : {scan_result.get('server')}",
        f"- Propulsé par : {scan_result.get('powered_by')}",
        f"- Type de contenu : {scan_result.get('content_type')}",
        "\n## En-têtes HTTP :"
    ]
    for k, v in scan_result.get("headers", {}).items():
        lines.append(f"- {k}: {v}")
    return "\n".join(lines)

def scan_target(target: str) -> str:
    scan_result = basic_host_info(target)
    report = format_report(scan_result)
    return report

# Test CLI
if __name__ == "__main__":
    target = "https://example.com"
    result = scan_target(target)
    print(result)
