from .AssignmentStatement import var
import writer

class MinusMinusStatement:
    def __init__(self, var):
        self.var = var
        self.op = "++"
    def execute(self):
        value = var.getType(self.var)
        if value not in ['str', 'bool']:
            writer.w(f"{self.var}.value--;")
        else:
            raise RuntimeError("This type don't support the -- operator")
