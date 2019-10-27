from .AssignmentStatement import var
import writer
from lib.RocTypes import getType

class VarCreateStatement:
    def __init__(self, var, type):
        self.var = var
        self.type = type

    def execute(self):
        var.set(self.var, "")
        writer.w(f"{self.type} {self.var};")

    def __str__(self):
        return "{} {}".format(self.type, self.var)