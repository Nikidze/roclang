import writer
from expressions.AssignmentStatement import var


class PrintStatement:
    def __init__(self, expression):
        self.expression = expression

    def execute(self):
        print(self.expression.__class__.__name__)
        if self.expression.__class__.__name__ == "VariablesExpression":
            if var.get(self.expression.name) == "array":
                writer.w(f"cout << {self.expression.name} << endl;")
                return
            if var.get(self.expression.name) == "function":
                writer.w(f"cout << {self.expression.name}().value << endl;")
                return
        elif self.expression.__class__.__name__ == "MethodCallExpression":
            writer.w(f"{self.expression.eval()};")
            writer.w(f"cout << {self.expression.var}.value << endl;")
        else:
            writer.w(f"cout << {self.expression.eval()}.value << endl;")