class NumberExpression:
    def __init__(self, value, is_dbl=False):
        self.value = value
        self.is_dbl = is_dbl

    def eval(self):
        if self.is_dbl:
            return f"DBL({self.value})"
        return f"INT({self.value})"
