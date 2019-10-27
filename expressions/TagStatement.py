import writer

class TagStatement:
    __slots__ = ['tag']

    def __init__(self, tag):
        self.tag = tag

    def execute(self):
        writer.w(f'cout << "{self.tag}";')