import requests

# Payloads classiques (XSS, SQLi, LFI…)
FUZZ_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "' OR '1'='1",
    "../../etc/passwd",
    "'; DROP TABLE users; --",
    "%00",
    "<img src=x onerror=alert(1)>"
]

def fuzz_url_get(url: str, param: str = "q"):
    """Test simple en GET sur un paramètre vulnérable simulé"""
    results = []

    for payload in FUZZ_PAYLOADS:
        test_url = f"{url}?{param}={payload}"
        try:
            r = requests.get(test_url, timeout=5)
            status = r.status_code
            text_snippet = r.text[:200].replace("\n", " ").replace("\r", "")
            results.append({
                "payload": payload,
                "url": test_url,
                "status": status,
                "response_preview": text_snippet
            })
        except Exception as e:
            results.append({
                "payload": payload,
                "url": test_url,
                "error": str(e)
            })

    return results

def format_fuzz_report(results: list) -> str:
    output = "# Rapport de Fuzzing basique\n"
    for res in results:
        output += f"\n## Test : {res['url']}\n"
        output += f"- Payload : `{res['payload']}`\n"
        if 'error' in res:
            output += f"- Erreur : {res['error']}\n"
        else:
            output += f"- Statut HTTP : {res['status']}\n"
            output += f"- Extrait de réponse :\n```\n{res['response_preview']}\n```\n"
    return output

# Test CLI
if __name__ == "__main__":
    url = "https://example.com/search"
    report = format_fuzz_report(fuzz_url_get(url, param="query"))
    print(report)
