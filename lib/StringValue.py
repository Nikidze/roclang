from decimal import Decimal


class StringValue:
    def __init__(self, value):
        self.value = value

    def asDouble(self):
        vstr = str(self.value)
        vstr = vstr.split(".")
        if len(vstr) == 2:
                return float(Decimal(self.value))
        return int(Decimal(self.value))

    def asString(self):
        return self.value

    def __str__(self):
        return self.value