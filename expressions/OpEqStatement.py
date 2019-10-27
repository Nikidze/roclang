import writer


class OpEqStatement:
    def __init__(self, var, operator, expression):
        self.var = var
        self.op = operator
        self.expression = expression

    def execute(self):
        writer.w(f"{self.var}.value {self.op}= {self.expression.eval()};")
