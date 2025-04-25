from web_navigator import fetch_and_summarize

def find_and_compare_tools(query: str, tools: list[str]) -> str:
    results = [fetch_and_summarize(tool) for tool in tools]
    return "\n---\n".join(results)

### Exemple :
# tools = ["https://chatgpt.com", "https://perplexity.ai", "https://www.deepl.com"]
# print(find_and_compare_tools("outils IA", tools))

