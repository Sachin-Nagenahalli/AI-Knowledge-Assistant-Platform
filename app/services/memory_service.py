class MemoryService:
    def __init__(self):
        self.messages = []

    def add_user(self, message: str):
        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    def add_assistant(self, message: str):
        self.messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def history(self):
        return self.messages[-10:]

    def clear(self):
        self.messages = []