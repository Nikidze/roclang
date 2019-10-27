class BinaryExpression:
    def __init__(self, operator, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
        self.operator = operator

    def eval(self):
        return f"{self.expr1.eval()}.value {self.operator} {self.expr2.eval()}.value"


    def __str__(self):
        return "({} {} {})".format(self.expr1, self.operator, self.expr2)
