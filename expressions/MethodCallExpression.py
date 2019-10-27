class MethodCallExpression:
    def __init__(self, var, method, args=None):
        self.var = var
        self.method = method
        self.args = args

    def eval(self):
        if self.args is not None:
            string = []
            for elm in self.args:
                string.append(elm.eval)
            string = ', '.join(string)
            return f"{self.var.eval()}.{self.method}({string})"
        return f"{self.var.eval()}.{self.method}()"
