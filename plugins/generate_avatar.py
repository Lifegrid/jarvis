from image_gen import text2im

def generate_avatar(name: str, style: str = "futuriste réaliste") -> str:
    prompt = generate_avatar_prompt(name, style)
    result = text2im(prompt=prompt, size="512x512")
    return result['images'][0] if result and "images" in result else "[Erreur génération]"
