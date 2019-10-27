def getType(var):
    typeVar = var.__class__.__name__
    return typeVar

def getNewType(type1, type2):
    if type1 == "int" and type2 == "int":
        return "int"
    if type1 == "float" and type2 == "float":
        return "float"
    if type1 == "int" and type2 == "float":
        return "float"
    if type1 == "float" and type2 == "int":
        return "float"
