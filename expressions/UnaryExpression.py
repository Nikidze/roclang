from lib.NumberValue import NumberValue


class UnaryExpression:
    def __init__(self, operator, expr1):
        self.expr1 = expr1
        self.operator = operator

    def eval(self):
        if self.operator == "-": return NumberValue(-self.expr1.eval.asDouble())
        if self.operator == "+": return NumberValue(self.expr1.eval.asDouble())


    def __str__(self):
        return "{}{}".format(self.operator, self.expr1.asString())