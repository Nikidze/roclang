from expressions.FunctionDefineStatement import f2

def w(str2):
    if not f2.f:
        f = open("main.txt", "a")
        f.write("{}\n".format(str2))
        f.close()
    else:
        f = open("func.txt", "a")
        f.write("{}\n".format(str2))
        f.close()
