from math import pi, e
from lib.NumberValue import NumberValue
import math


class sin:
    def execute(self, args=list()):
        if len(args) != 1:
            raise RuntimeError("One args expected")
        return NumberValue(math.sin(args[0].asDouble()))
class echo:
    def execute(self, args=list()):
        for arg in args:
            print(arg.asString())
        return NumberValue(0)

class Functions:

    ZERO = NumberValue(0)

    def __init__(self):
        self.functions = dict()
        self.functions["sin"] = sin()
        self.functions["echo"] = echo()

    def isExists(self, name):
        if name in self.functions:
            return True
        return False

    def get(self, key):
        try:
            return self.functions[key]
        except KeyError:
            raise RuntimeError("Unknown function" + key)

    def set(self, name, function):
        self.functions[name] = function

