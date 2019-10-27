class ArrayExpression:
    def __init__(self, array=[], autofill=False, start=0, step=1, stop=0):
        self.array = array
        self.autofill = autofill
        self.start = start
        self.step = step
        self.stop = stop

    def eval(self):
        if self.autofill:
            return 0
        string = []
        for elm in self.array:
            string.append(elm.eval())
        string = ', '.join(string)
        return string, len(self.array)
