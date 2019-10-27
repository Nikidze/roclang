from enum import Enum



class OPERATOR(Enum):
    PLUS, MINUS, MULTIPLY, DIVIDE, EQUALS, NOT_EQUALS, LT, LTEQ, GT, GTEQ, AND, OR = range(12)