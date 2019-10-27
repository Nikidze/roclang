class StringExpression:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return f"STR(\"{self.value}\")"
