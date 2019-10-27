import writer

class BreakStatement(RuntimeError):

    def execute(self):
        writer.w("break;")

    def __str__(self):
        return "break"
