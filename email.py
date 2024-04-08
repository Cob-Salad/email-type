class Email:
    def __init__(self, content: str):
        self.content = content

    def __str__(self) -> str:
        return self.content
