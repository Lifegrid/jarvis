# voice_interface/text_to_speech.py

import pyttsx3

def speak(text: str, voice_gender: str = "male"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Sélectionne une voix masculine ou féminine selon les paramètres disponibles
    for voice in voices:
        if voice_gender == "male" and "male" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
        elif voice_gender == "female" and "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 160)  # Vitesse de la voix
    engine.say(text)
    engine.runAndWait()
