def getType(type1, type2 = 0):
    if self.expression.__class__.__name__ == "BinaryExpression":
        type = self.expression.getType()
        return type
    elif result.__class__.__name__ == "NumberValue":
        if len(str(result).split(".")) == 1:
            return "int"
        else:
            return "float"
    elif result.__class__.__name__ == "str":
        return "string"