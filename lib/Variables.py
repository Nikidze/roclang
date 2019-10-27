class Variables:
    stack = {}

    def __init__(self):
        self.types = {}

    def get(self, key):
        try:
            return self.types[key]
        except KeyError:
            return "var"

    def set(self, name, type):
        self.types[name] = type

