import writer

class InputStatement:
    def __init__(self, expression):
        self.expression = expression

    def execute(self):
        if self.expression.__class__.__name__ == "VariablesExpression":
            writer.w(f"cin >> {self.expression.eval()};")
        else:
            writer.w(f"cin >> {self.expression.eval()};")

    def __str__(self):
        return "{} {}".format("print", self.expression)