from lib.NumberValue import NumberValue
from .BreakStatement import BreakStatement

class SwitchStatement:
    values = []
    statements = []

    def __init__(self, matching, br):
        self.matching = matching
        self.br = br

    def add(self, value, statement):
        self.values.append(value)
        self.statements.append(statement)

    def execute(self):
        varname = self.matching.eval
        if varname.__class__.__name__ == "StringValue":
            varvalue = varname.asString()
            step = 0
            for value in self.values:
                if varvalue == NumberValue(value).asString():
                    if self.br:
                        self.statements[step].execute()
                        break
                    else:
                        try:
                            self.statements[step].execute()
                        except BreakStatement:
                            break
                step += 1
            return
        if varname.__class__.__name__ == "NumberValue":
            varvalue = varname.asDouble()
            step = 0
            for value in self.values:
                if varvalue == NumberValue(value).asDouble():
                    if self.br:
                        self.statements[step].execute()
                        break
                    else:
                        try:
                            self.statements[step].execute()
                        except BreakStatement:
                            break
            step += 1
            return
