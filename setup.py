from setuptools import setup, find_packages

setup(
    name='jarvis_ai',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'fastapi',
        'uvicorn',
        'ollama',
        'openai',
        'torch',
        'whisper',
        'chromadb',
        'faiss-cpu',
        'pyaudio',
        'sounddevice',
        'pyttsx3',
        'requests',
        'python-dotenv',
        'playwright',
        'selenium',
        'pywinauto',
        'typer'
    ],
    entry_points={
        'console_scripts': [
            'jarvis=core_llm.interpreter:main'
        ]
    }
)
