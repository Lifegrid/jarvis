# core_llm/thread_handler.py

class ThreadHandler:
    def __init__(self, system_prompt=None, max_history=10):
        """
        Initialise une session de conversation avec mémoire.
        """
        self.max_history = max_history
        self.messages = []
        if system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})
        self._trim()

    def add_ai_response(self, content):
        self.messages.append({"role": "assistant", "content": content})
        self._trim()

    def get_context(self):
        return self.messages

    def _trim(self):
        # Garde seulement les X derniers échanges (pairs user + AI)
        while len(self.messages) > self.max_history * 2:
            # Si le 1er est un prompt système, on le garde
            if self.messages[0]["role"] == "system":
                self.messages = [self.messages[0]] + self.messages[2:]
            else:
                self.messages = self.messages[2:]
