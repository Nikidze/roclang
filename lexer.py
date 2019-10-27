from token import Token, TokenType


class Lexer:
    tokens = []

    OPERATOR_CHARS = "+-*/(){}[]=<>!&|;,.:"

    OPERATORS = {
        "+": TokenType.PLUS,
        "++": TokenType.PLUSPLUS,
        "+=": TokenType.PLUSEQ,
        "-": TokenType.MINUS,
        "--": TokenType.MINUSMINUS,
        "-=": TokenType.MINUSEQ,
        "*": TokenType.STAR,
        "*=": TokenType.STAREQ,
        "/": TokenType.SLASH,
        "/=": TokenType.SLASHEQ,
        "(": TokenType.LPAREN,
        "[": TokenType.LSQBR,
        "]": TokenType.RSQBR,
        ")": TokenType.RPAREN,
        "{": TokenType.LBRACE,
        "}": TokenType.RBRACE,
        "=": TokenType.EQ,
        "<": TokenType.LT,
        ">": TokenType.GT,
        ";": TokenType.SEMICOLON,
        ":": TokenType.COLON,
        ",": TokenType.COMMA,
        "!": TokenType.EXCL,
        "&": TokenType.AMP,
        "|": TokenType.BAR,
        "==": TokenType.EQEQ,
        "!=": TokenType.EXCLEQ,
        "<=": TokenType.LTEQ,
        ">=": TokenType.GTEQ,
        "||": TokenType.BARBAR,
        "&&": TokenType.AMPAMP,
    }

    Types = ['int', 'dbl', 'bool', 'str', 'int_arr', 'str_arr']

    pos = 0

    def __init__(self, input):
        self.input = input
        self.length = len(input)
        self.tokens = []

    def tokenize(self):
        while self.pos < self.length:
            ch = self.peek(0)
            if ch.isdigit():
                self.tokenizeNumber()
            elif ch.isalpha():
                self.tokenizeWord()
            elif ch == '"' or ch == "$":
                self.tokenizeText()
            elif ch in self.OPERATOR_CHARS:
                self.tokenizeOperator()
            else:
                self.next()
        return self.tokens

    def tokenizeNumber(self):
        current = self.peek(0)
        string = ''
        is_dbl = False
        while True:
            if current == '.' and self.peek(1) != ".":
                if self.peek(1).isalpha():
                    if is_dbl:
                        self.addToken(TokenType.DBLNUMBER, string)
                    else:
                        self.addToken(TokenType.NUMBER, string)
                    self.addToken(TokenType.POINT)
                    self.next()
                    return
                else:
                    is_dbl = True
                if not string.find('.'):
                    raise Exception("Invalid float number")
            elif not current.isdigit():
                break
            string = '{}{}'.format(string, current)
            current = self.next()
        if is_dbl:
            self.addToken(TokenType.DBLNUMBER, string)
            return
        self.addToken(TokenType.NUMBER, string)

    def tokenizeWord(self):
        current = self.peek(0)
        string = ''
        while True:
            if current.isdigit() or current.isalpha() or current == "_":
                string = '{}{}'.format(string, current)
                current = self.next()
                continue
            break
        if current == ":":
            self.addToken(TokenType.WORD, string)
            self.next()
            self.tokenizeWord()
        elif string == "print":
            self.addToken(TokenType.PRINT)
        elif string == "input":
            self.addToken(TokenType.INPUT)
        elif string == "import":
            self.addToken(TokenType.IMPORT)
        elif string == "if":
            self.addToken(TokenType.IF)
        elif string == "else":
            self.addToken(TokenType.ELSE)
        elif string == "while":
            self.addToken(TokenType.WHILE)
        elif string == "for":
            self.addToken(TokenType.FOR)
        elif string == "do":
            self.addToken(TokenType.DO)
        elif string == "break":
            self.addToken(TokenType.BREAK)
        elif string == "continue":
            self.addToken(TokenType.CONTINUE)
        elif string == "switch":
            self.addToken(TokenType.SWITCH)
        elif string == "switchbreak":
            self.addToken(TokenType.SWITCHBREAK)
        elif string == "def":
            self.addToken(TokenType.DEF)
            if self.peek(0) == ":":
                self.next()
                self.tokenizeWord()
        elif string == "return":
            self.addToken(TokenType.RETURN)
        elif string == "end":
            self.addToken(TokenType.END)
        elif string in self.Types:
            self.addToken(TokenType.VARTYPE, string.upper())
        else:
            self.addToken(TokenType.WORD, string)

    def tokenizeText(self):
        if self.peek(0) == "$":
            if self.peek(1).isalpha():
                string = ''
                current = self.next()
                while current not in ['\r', '\n', '\0', '/0', " ", "."]:
                    string += current
                    current = self.next()
                self.addToken(TokenType.TEXT, string)
                return
        self.next()
        current = self.peek(0)
        string = ''
        while True:
            if current == "\\":
                current = self.next()
                if current == '"':
                    string = '{}{}'.format(string, '"')
                    current = self.next()
                    continue
                if current == 'n':
                    string = '{}{}'.format(string, '\n')
                    current = self.next()
                    continue
                if current == 't':
                    string = '{}{}'.format(string, '\t')
                    current = self.next()
                    continue
                string = '{}{}'.format(string, '\\')
                continue

            if current == '"':
                break
            string = '{}{}'.format(string, current)
            current = self.next()
        self.next()
        self.addToken(TokenType.TEXT, string)

    def tokenizeOperator(self):
        current = self.peek(0)
        if current == '/':
            next = self.peek(1)
            if next == '/':
                self.next()
                self.next()
                self.tokenizeComment()
                return
            elif next == '*':
                self.next()
                self.next()
                self.tokenizeMultilineComment()
                return
            elif next == "=":
                self.addToken(TokenType.SLASHEQ)
                self.next()
                self.next()
                return

        if current == "+":
            next = self.peek(1)
            if next == "+":
                self.addToken(TokenType.PLUSPLUS)
                self.next()
                self.next()
                return
            if next == "=":
                self.addToken(TokenType.PLUSEQ)
                self.next()
                self.next()
                return
        if current == "-":
            next = self.peek(1)
            if next == "-":
                self.addToken(TokenType.MINUSMINUS)
                self.next()
                self.next()
                return
            if next == "=":
                self.addToken(TokenType.MINUSEQ)
                self.next()
                self.next()
                return
        if current == "*":
            next = self.peek(1)
            if next == "=":
                self.addToken(TokenType.STAREQ)
                self.next()
                self.next()
                return
        if current == ".":
            if self.peek(1) == ".":
                if self.peek(2) == ".":
                    self.addToken(TokenType.TRPOINT)
                    self.next()
                    self.next()
                    self.next()
                else:
                    self.addToken(TokenType.DBPOINT)
                    self.next()
                    self.next()
            else:
                self.addToken(TokenType.POINT)
                self.next()
            return
        if current == ":":
            if self.peek(1) == "\n":
                self.addToken(TokenType.COLON)
                self.addToken(TokenType.NEWSTR)
                self.next()
            return
        string = ''
        while True:
            text = string
            if "{}{}".format(text, current) not in self.OPERATORS and text != '':
                self.addToken(self.OPERATORS[text])
                return
            string = "{}{}".format(string, current)
            current = self.next()

    def peek(self, relativePosition):
        position = self.pos + relativePosition
        if position >= self.length:
            return '/0'
        return self.input[position]

    def next(self):
        self.pos += 1
        return self.peek(0)

    def addToken(self, type, text=""):
        self.tokens.append(Token(type, text))

    def tokenizeMultilineComment(self):
        current = self.peek(0)
        while True:
            if current == '\0':
                raise RuntimeError("Missing close tag")
            if current == '*' and self.peek(1) == '/':
                break
            current = self.next()
        self.next()
        self.next()

    def tokenizeComment(self):
        current = self.peek(0)
        while current not in ['\r', '\n', '\0', '/0']:
            current = self.next()
