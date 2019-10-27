from tokentype import TokenType


class Token:
    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return "{} {}".format(self.type, self.text)
