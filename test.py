from lexer import Lexer
from parser import Parser
import os

open("func.txt", "w").close()
open("main.txt", "w").close()
program = open("test.roc").read()


tokens = Lexer(program).tokenize()
for token in tokens:
    print(token)
program = Parser(tokens).parse()
program.execute()
print("----------------------------------------")
start = open("roc.cpp").read()
f2 = open("com.cpp", "w")
f2.write(start)
f2.close()
f2 = open("com.cpp", "a")
f2.write(open("func.txt", "r").read() + "\n")
f2.write("int main(){\n" + open("main.txt", "r").read())
f2.write("return 0;\n}\n")
f2.close()
os.system("g++ com.cpp -o com.out")
os.system("./com.out")
"""