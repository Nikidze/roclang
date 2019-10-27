from lib.NumberValue import NumberValue
from .operators import OPERATOR

class ConditionalExpression:
    def __init__(self, operator, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
        self.operator = operator


    def getOperator(self):
        if self.opIs(OPERATOR.LT):
            result = "<"
        elif self.opIs(OPERATOR.GT):
            result = ">"
        elif self.opIs(OPERATOR.EQUALS):
            result = "=="
        if self.opIs(OPERATOR.LTEQ):
            result = "<+"
        elif self.opIs(OPERATOR.GTEQ):
            result = ">="
        elif self.opIs(OPERATOR.AND):
            result = "&&"
        elif self.opIs(OPERATOR.OR):
            result = "||"
        elif self.opIs(OPERATOR.NOT_EQUALS):
            result = "!="
        return result

    def compareTo(self, str1, str2):
        if str1 < str2:
            return -1
        elif str1 > str2:
            return 1
        elif str1 == str2:
            return 0

    def opIs(self, op):
        if self.operator == op:
            return True
        return False

    def eval(self):
        expr1 = self.expr1.eval()
        expr2 = self.expr2.eval()
        return f"{expr1} {self.getOperator()} {expr2}"

    def __str__(self):
        return "({} {} {})".format(self.expr1, self.operator, self.expr2)
