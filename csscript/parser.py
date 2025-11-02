from ast import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', None)

    def eat(self, token_type):
        kind, value = self.current_token()
        if kind == token_type:
            self.pos += 1
            return value
        else:
            raise SyntaxError(f"Expected {token_type} but got {kind}")

    def parse(self):
        nodes = []
        while self.pos < len(self.tokens):
            node = self.statement()
            nodes.append(node)
        return nodes

    def statement(self):
        kind, _ = self.current_token()
        if kind == 'ID':
            # assignment
            name = self.eat('ID')
            self.eat('ASSIGN')
            expr = self.expr()
            return Assign(name, expr)
        elif kind == 'PRINT':
            self.eat('PRINT')
            expr = self.expr()
            return Print(expr)
        else:
            raise SyntaxError('Unknown statement')

    def expr(self):
        left = self.term()
        while self.current_token()[0] == 'OP':
            op = self.eat('OP')
            right = self.term()
            left = BinOp(left, op, right)
        return left

    def term(self):
        kind, value = self.current_token()
        if kind == 'NUMBER':
            self.eat('NUMBER')
            return Num(value)
        elif kind == 'ID':
            name = self.eat('ID')
            return Var(name)
        else:
            raise SyntaxError('Expected number or identifier')
