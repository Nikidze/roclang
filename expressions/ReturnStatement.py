import writer


class ReturnStatement:

    def __init__(self, expression):
        self.expression = expression
        self.result = None

    def execute(self):
        self.result = "" if self.expression.__class__.__name__ == "NoneExpression" else self.expression.eval()
        writer.w(f"return {self.result};")
