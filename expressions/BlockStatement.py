class BlockStatement:

    def __init__(self):
        self.statements = []

    def add(self, statement):
        self.statements.append(statement)

    def execute(self):
        for statement in self.statements:
            statement.execute()

    def __str__(self):
        string = ''
        for statement in self.statements:
            string = '{}{}\n'.format(string, statement.__str__)
        return string