import writer


class ContinueStatement(RuntimeError):
    def execute(self):
        writer.w("continue;")

    def __str__(self):
        return "continue"
