from expressions.BreakStatement import BreakStatement
from expressions.ContinueStatement import ContinueStatement
import writer

class ForStatement:
    def __init__(self, initialization, termination, increment, block):
        self.initialization = initialization
        self.termination = termination
        self.increment = increment
        self.block = block

    def execute(self):
        var = self.initialization.var
        result = self.initialization.expression.eval
        writer.w(f"for(double {var} = {result}; {self.termination.expr1} {self.termination.getOperator()} {self.termination.expr2}; {self.increment.var}{self.increment.op}){'{'}")
        try:
             self.block.execute()
        except BreakStatement:
            writer.w("break;")
        except ContinueStatement:
            writer.w("continue;")
        writer.w("}")

    def __str__(self):
        return "for {} {}".format(self.initialization, self.block)