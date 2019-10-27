import writer


class FunctionalStatement:
    def __init__(self, func):
        self.func = func

    def execute(self):
        writer.w(f"{self.func.eval()};")
