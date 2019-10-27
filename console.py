from lexer import Lexer
from parser import Parser
import os


while True:
    expression = input(">>>")
    if expression == "exit":
        break
    open("main.txt", "w").close()

    start = """#include <iostream>
    using namespace std;
    #include "Functions/TypeConversion.h"
    #include <cmath>
    """

    f2 = open("com.cpp", "w")
    f2.write(start)
    f2.close()
    tokens = Lexer(expression).tokenize()
    program = Parser(tokens).parse()
    program.execute()

    f2 = open("com.cpp", "a")
    f2.write(open("func.txt", "r").read() + "\n")
    f2.write("int main(){\n" + open("main.txt", "r").read())
    f2.write("return 0;\n}\n")
    f2.close()
    os.system("g++ com.cpp -o com.out")
    os.system("./com.out")
    continue