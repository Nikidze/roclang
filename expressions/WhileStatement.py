import writer


class WhileStatement:
    def __init__(self, conditional, statement):
        self.conditional = conditional
        self.statement = statement

    def execute(self):
        writer.w(f"while({self.conditional.eval()}){'{'}")
        self.statement.execute()
        writer.w("}")

    def __str__(self):
        return "while {} {}".format(self.conditional, self.statement)