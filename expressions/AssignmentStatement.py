from lib import Variables as v
import writer

var = v.Variables()


class AssignmentStatement:
    def __init__(self, var, expression, type = ""):
        self.var = var
        self.expression = expression
        self.type = type

    def execute(self):
        if self.type != "":
            if self.expression != None:
                if self.expression.__class__.__name__ == "ArrayExpression":
                    var.set(self.var, "array")
                    if self.expression.autofill:
                        writer.w(f"vector<INT> {self.var}_v;")
                        writer.w(f"for(int i = {self.expression.start.eval()}; i <= {self.expression.stop.eval()}; i += {self.expression.step.eval()}){'{'}")
                        writer.w(f"{self.var}_v.push_back(i);")
                        writer.w("}")
                        writer.w(f"{self.type} {self.var} = INT_ARR({self.var}_v);")
                    else:
                        result = self.expression.eval()
                        writer.w(f"INT {self.var}_arr[{result[1]}] = {'{'}{result[0]}{'}'};")
                        writer.w(f"vector<INT> {self.var}_v({self.var}_arr,{self.var}_arr+{result[1]});")
                        writer.w(f"{self.type} {self.var} = INT_ARR({self.var}_v);")
                else:
                    result = self.expression.eval()
                    writer.w(f"{self.type} {self.var} = {result};")
            else:
                writer.w(f"{self.type} {self.var};")
        else:
            result = self.expression.eval()
            writer.w(f"{self.var} = {result};")
