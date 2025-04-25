import socket
import requests
from urllib.parse import urlparse

def scan_ports(domain: str, ports=[80, 443, 22, 21, 3306]) -> str:
    report = []
    for port in ports:
        try:
            sock = socket.create_connection((domain, port), timeout=1)
            report.append(f"✅ Port {port} ouvert")
            sock.close()
        except:
            report.append(f"❌ Port {port} fermé")
    return "\n".join(report)

def get_headers(domain: str) -> str:
    try:
        res = requests.get(f"http://{domain}", timeout=3)
        headers = "\n".join(f"{k}: {v}" for k, v in res.headers.items())
        return f"✅ Headers HTTP:\n{headers}"
    except Exception as e:
        return f"❌ Impossible de récupérer les headers: {e}"

def security_scan(domain: str) -> list[str]:
    return [
        get_headers(domain),
        scan_ports(domain)
    ]
