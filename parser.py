from expressions.ArrayVariableExpression import ArrayVariablesExpression
from expressions.TagStatement import TagStatement
from lexer import Lexer
from expressions.FunctionDefineStatement import FunctionDefineStatement
from expressions.FunctionalStatement import FunctionalStatement
from expressions.InputStatement import InputStatement
from expressions.ReturnStatement import ReturnStatement
from token import Token, TokenType
from expressions.NumberExpression import NumberExpression
from expressions.BinaryExpression import BinaryExpression
from expressions.UnaryExpression import UnaryExpression
from expressions.VariablesExpression import VariablesExpression
from expressions.AssignmentStatement import AssignmentStatement, var
from expressions.PrintStatement import PrintStatement
from expressions.StringExpression import StringExpression
from expressions.ConditionalExpression import ConditionalExpression
from expressions.IfStatement import IfStatement
from expressions.ConditionalExpression import OPERATOR
from expressions.BlockStatement import BlockStatement
from expressions.WhileStatement import WhileStatement
from expressions.ForStatement import ForStatement
from expressions.BreakStatement import BreakStatement
from expressions.ContinueStatement import ContinueStatement
from expressions.FunctionalExpression import FunctionalExpressions
from expressions.PlusPlusStatement import PlusPlusStatement
from expressions.MinusMinusStatement import MinusMinusStatement
from expressions.OpEqStatement import OpEqStatement
from expressions.switchStatement import SwitchStatement
from expressions.MethodCallExpression import MethodCallExpression
from expressions.ArrayExpression import ArrayExpression
from expressions.NoneExpression import NoneExpression

class Parser:
    GLOBAL_CALL = ""
    pos = 0
    EOF = Token(TokenType.EOF, "")
    TYPES = ['int', 'dbl', 'bool', 'str', 'int_arr']

    def __init__(self, tokens):
        self.tokens = tokens
        self.size = len(tokens)

    def parse(self):
        result = BlockStatement()
        while not self.match(TokenType.EOF):
            result.add(self.statement)
        return result

    def match(self, type):
        current = self.get(0)
        if current.type != type:
            return False
        self.pos += 1
        return True

    def consume(self, type):
        current = self.get(0)
        if current.type != type:
            raise RuntimeError("Token {} doesn't match {}".format(current, type))
        self.pos += 1
        return current

    def block(self):
        block = BlockStatement()
        while not self.match(TokenType.END):
            block.add(self.statement)
        return block

    def statementOrBlock(self):
        if self.match(TokenType.COLON) and self.match(TokenType.NEWSTR):
            return self.block()
        return self.statement()

    @property
    def statement(self):
        if self.match(TokenType.PRINT):
            return PrintStatement(self.expression())
        elif self.match(TokenType.INPUT):
            return InputStatement(self.expression())
        elif self.match(TokenType.IF):
            return self.ifElse()
        elif self.match(TokenType.WHILE):
            return self.whileStatement()
        elif self.match(TokenType.BREAK):
            return BreakStatement()
        elif self.match(TokenType.CONTINUE):
            return ContinueStatement()
        elif self.match(TokenType.RETURN):
            self.GLOBAL_CALL = "ReturnStatement"
            return ReturnStatement(self.expression())
        elif self.match(TokenType.FOR):
            return self.forStatement()
        elif self.match(TokenType.SWITCH):
            return self.switchStatement()
        elif self.match(TokenType.SWITCHBREAK):
            return self.switchStatement(True)
        elif self.match(TokenType.IMPORT):
            return self.importStatement()
        elif self.match(TokenType.DEF):
            return self.functionDefine()
        elif self.get(0).type == TokenType.TAG:
            return TagStatement(self.consume(TokenType.TAG).text)
        elif self.get(0).type == TokenType.WORD and self.get(1).type == TokenType.LPAREN:
            return FunctionalStatement(self.function())
        # TODO продумать, нужна ли реализация ArrayStatement, как здесь (FunctionalStatement)
        vartype = var.get(self.get(0).text)
        if vartype == "function":
            return FunctionalStatement(self.function(noArg=True))
        return self.assignmentstatement()

    def assignmentstatement(self, array=''):
        current = self.get(0)
        var = current.text
        if array != '':
            current.type = TokenType.WORD
            var = array
        if current.type == TokenType.WORD:
            if self.get(1).type == TokenType.EQ:
                self.consume(TokenType.WORD)
                self.consume(TokenType.EQ)
                return AssignmentStatement(var, self.expression())
            elif self.get(1).type == TokenType.PLUSPLUS:
                self.consume(TokenType.WORD)
                self.consume(TokenType.PLUSPLUS)
                return PlusPlusStatement(var)
            elif self.get(1).type == TokenType.MINUSMINUS:
                self.consume(TokenType.WORD)
                self.consume(TokenType.MINUSMINUS)
                return MinusMinusStatement(var)
            elif self.get(1).type == TokenType.PLUSEQ:
                self.consume(TokenType.WORD)
                self.consume(TokenType.PLUSEQ)
                return OpEqStatement(var, "+", self.expression())
            elif self.get(1).type == TokenType.MINUSEQ:
                self.consume(TokenType.WORD)
                self.consume(TokenType.MINUSEQ)
                return OpEqStatement(var, "-", self.expression())
            elif self.get(1).type == TokenType.STAREQ:
                self.consume(TokenType.WORD)
                self.consume(TokenType.STAREQ)
                return OpEqStatement(var, "*", self.expression())
            elif self.get(1).type == TokenType.SLASHEQ:
                self.consume(TokenType.WORD)
                self.consume(TokenType.SLASHEQ)
                return OpEqStatement(var, "/", self.expression())
            elif self.get(1).type == TokenType.LSQBR:
                name = self.consume(TokenType.WORD)
                self.consume(TokenType.LSQBR)
                number = self.expression()
                return self.assignmentstatement(array=f"{name.text}[{number.eval}]")
            elif self.get(1).type == TokenType.VARTYPE:
                varName = self.consume(TokenType.WORD).text
                vatType = self.consume(TokenType.VARTYPE).text
                if self.match(TokenType.EQ):
                    return AssignmentStatement(varName, self.expression(), vatType)
                else:
                    return AssignmentStatement(varName, None, vatType)

        raise RuntimeError("Unknown statement")

    def ifElse(self):
        condition = self.expression()
        ifStatement = self.statementOrBlock()
        elseStatement = None
        if self.match(TokenType.ELSE):
            elseStatement = self.statementOrBlock()
        return IfStatement(condition, ifStatement, elseStatement)

    def switchStatement(self, br=False):
        matching = self.expression()
        self.consume(TokenType.LBRACE)
        switch = SwitchStatement(matching, br)
        while not self.match(TokenType.RBRACE):
            current = self.get(0)
            if self.match(TokenType.NUMBER):
                statement = self.statementOrBlock()
                switch.add(current.text, statement)
                continue
            if self.match(TokenType.TEXT):
                statement = self.statementOrBlock()
                switch.add(current.text, statement)
                continue
        return switch

    def whileStatement(self):
        condition = self.expression()
        statement = self.statementOrBlock()
        return WhileStatement(condition, statement)

    def forStatement(self):
        initialization = self.assignmentstatement()
        self.consume(TokenType.SEMICOLON)
        termination = self.expression()
        self.consume(TokenType.SEMICOLON)
        increment = self.assignmentstatement()
        statement = self.statementOrBlock()
        return ForStatement(initialization, termination, increment, statement)

    def importStatement(self):
        file = self.consume(TokenType.WORD)
        file = file.text
        print(file, "----------------------------------")
        tokens = Lexer(open(f"{file}.roc").read()).tokenize()
        for token in tokens:
            print(token)
        print(file, "----------------------------------")
        program = Parser(tokens).parse()
        return program

    def methodExpression(self, current):
        method = self.get(1)
        self.match(TokenType.WORD)
        self.match(TokenType.POINT)
        self.match(TokenType.WORD)
        if self.match(TokenType.LPAREN):
            args = []
            while not (self.match(TokenType.RPAREN) or self.match(TokenType.EOF)):
                args.append(self.expression())
                self.match(TokenType.COMMA)
            return MethodCallExpression(current, method.text, args)
        else:
            return MethodCallExpression(current, method.text)

    def arrayStatement(self):
        array = []
        if self.get(1).type == TokenType.DBPOINT:
            start = self.expression()
            self.consume(TokenType.DBPOINT)
            stop = self.expression()
            step = NumberExpression(1)
            if self.match(TokenType.DBPOINT):
                step = stop
                stop = self.expression()
            self.consume(TokenType.RSQBR)
            return ArrayExpression(autofill=True, start=start, step=step, stop=stop)
        while not (self.match(TokenType.RSQBR) or self.match(TokenType.EOF)):
            array.append(self.expression())
            self.match(TokenType.COMMA)
        return ArrayExpression(array=array)

    def function(self, noArg=False):
        name = self.consume(TokenType.WORD).text
        if noArg:
            return FunctionalExpressions(name)
        self.consume(TokenType.LPAREN)
        function = FunctionalExpressions(name)
        while not self.match(TokenType.RPAREN):
            function.addArg(self.expression())
            self.match(TokenType.COMMA)
        return function

    def functionDefine(self):
        name = self.consume(TokenType.WORD).text
        functype = self.consume(TokenType.VARTYPE).text if self.get(0).type == TokenType.VARTYPE else "void"
        self.consume(TokenType.LPAREN)
        args = []
        while not self.match(TokenType.RPAREN):
            varName = self.consume(TokenType.WORD).text
            varType = self.consume(TokenType.VARTYPE).text
            args.append(varType)
            args.append(varName)
            self.match(TokenType.COMMA)
        body = self.statementOrBlock()
        return FunctionDefineStatement(functype, name, args, body)

    def expression(self):
        return self.logicalOr()

    def logicalOr(self):
        result = self.logicalAnd()
        while True:
            if self.match(TokenType.BARBAR):
                result = ConditionalExpression(OPERATOR.OR, result, self.logicalAnd())
                continue
            break
        return result

    def logicalAnd(self):
        result = self.equality()
        while True:
            if self.match(TokenType.AMPAMP):
                result = ConditionalExpression(OPERATOR.AND, result, self.equality())
                continue
            break
        return result

    def equality(self):
        result = self.conditional()

        if self.match(TokenType.EQEQ):
            return ConditionalExpression(OPERATOR.EQUALS, result, self.conditional())
        if self.match(TokenType.EXCLEQ):
            return ConditionalExpression(OPERATOR.NOT_EQUALS, result, self.conditional())

        return result

    def conditional(self):
        result = self.additive()

        while True:
            if self.match(TokenType.LT):
                result = ConditionalExpression(OPERATOR.LT, result, self.additive())
                continue
            if self.match(TokenType.LTEQ):
                result = ConditionalExpression(OPERATOR.LTEQ, result, self.additive())
                continue
            if self.match(TokenType.GT):
                result = ConditionalExpression(OPERATOR.GT, result, self.additive())
                continue
            if self.match(TokenType.GTEQ):
                result = ConditionalExpression(OPERATOR.GTEQ, result, self.additive())
                continue
            break

        return result

    def additive(self):
        result = self.multiplicative()

        while True:
            if self.match(TokenType.PLUS):
                result = BinaryExpression("+", result, self.multiplicative())
                continue
            if self.match(TokenType.MINUS):
                result = BinaryExpression("-", result, self.multiplicative())
                continue
            break

        return result

    def multiplicative(self):
        result = self.unary()

        while True:
            if self.match(TokenType.STAR):
                result = BinaryExpression("*", result, self.unary())
                continue
            if self.match(TokenType.SLASH):
                result = BinaryExpression("/", result, self.unary())
                continue
            break

        return result

    def unary(self):
        if self.match(TokenType.MINUS):
            return UnaryExpression("-", self.primary())
        if self.match(TokenType.PLUS):
            return self.primary()
        return self.primary()

    def primary(self):
        current = self.get(0)
        if self.match(TokenType.NUMBER):
            if self.get(0).type == TokenType.POINT:
                if self.get(1).type == TokenType.WORD:
                    return self.methodExpression(NumberExpression(current.text))
            return NumberExpression(current.text)
        if self.match(TokenType.DBLNUMBER):
            if self.get(0).type == TokenType.POINT:
                if self.get(1).type == TokenType.WORD:
                    return self.methodExpression(NumberExpression(current.text, is_dbl=True))
            return NumberExpression(current.text, is_dbl=True)
        elif current.type == TokenType.WORD and self.get(1).type == TokenType.LPAREN:
            return self.function()
        elif current.type == TokenType.WORD and self.get(1).type == TokenType.LSQBR:
            name = self.consume(TokenType.WORD)
            self.consume(TokenType.LSQBR)
            number = self.expression()
            self.consume(TokenType.RSQBR)
            return ArrayVariablesExpression(name.text, number)
        elif self.match(TokenType.WORD):
            if self.get(0).type == TokenType.POINT:
                if self.get(1).type == TokenType.WORD:
                    return self.methodExpression(VariablesExpression(current.text))
            return VariablesExpression(current.text)
        elif self.match(TokenType.TEXT):
            if self.get(0).type == TokenType.POINT:
                if self.get(1).type == TokenType.WORD:
                    return self.methodExpression(StringExpression(current.text))
            return StringExpression(current.text)
        elif self.match(TokenType.LPAREN):
            result = self.expression()
            self.match(TokenType.RPAREN)
            return result
        elif self.match(TokenType.LSQBR):
            result = self.arrayStatement()
            return result
        elif self.GLOBAL_CALL == "ReturnStatement":
            self.GLOBAL_CALL = ""
            return NoneExpression()
        raise Exception("Unknown expression")

    def get(self, relativePosition):
        position = self.pos + relativePosition
        if position >= self.size:
            return self.EOF
        return self.tokens[position]
