import lib.Functions as lf

Functions = lf.Functions()


class FunctionalExpressions:

    def __init__(self, name, args=list()):
        self.name = name
        self.args = args

    def addArg(self, arg):
        self.args.append(arg)

    def eval(self):
        name = self.name
        args1 = self.args
        args = ""
        for arg in args1:
            args += str(arg.eval()) + ", "
        args = args[:-2]
        return f"{name}({args})"

    def __str__(self):
        return self.name + "(" + str(self.args) + ")"
