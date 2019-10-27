import writer

class IfStatement:

    def __init__(self, expression, ifStatement, elseStatement):
        self.expression = expression
        self.ifStatement = ifStatement
        self.elseStatement = elseStatement

    def execute(self):
        writer.w(f"if({self.expression.eval()}){'{'}")
        self.ifStatement.execute()
        if self.elseStatement != None:
            writer.w("}else{")
            self.elseStatement.execute()
        writer.w("}")

    def __str__(self):
        string = ''
        string = "if {} {}".format(self.expression, self.ifStatement)
        if self.elseStatement != None:
            string = "{}\nelse {}".format(string, self.elseStatement)
        return string