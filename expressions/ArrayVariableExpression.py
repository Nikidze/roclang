class ArrayVariablesExpression:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def eval(self):
        return f"{self.name}[{self.number.eval()}].value"
