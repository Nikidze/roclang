from func import f
from expressions.AssignmentStatement import var

f2 = f()


class FunctionDefineStatement:
    def __init__(self,functype, name, args, body):
        self.functype = functype
        self.name = name
        self.args = args
        self.body = body
        var.set(self.name, "function")

    def execute(self):
        # TODO разобраться в этом, подкоректировать не нужное
        f2.f = True
        args = ""
        i = 0
        l = len(self.args)
        while i <= l - 1:
            args += f"{self.args[i]} { self.args[i+1]}, "
            i += 2
        open("func.txt", "a").write(f"{self.functype} {self.name} ({args[:-2]})" + "{\n")
        self.body.execute()
        f2.f = False
        open("func.txt", "a").write("}")

    def __str__(self):
        return "def (" + self.args.__str__ + ") " + self.body.__str__
