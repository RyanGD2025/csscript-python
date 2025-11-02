import re

TOKEN_SPECIFICATION = [
    ('NUMBER',   r'd+(.d*)?'),  # Integer or decimal number
    ('ASSIGN',   r'='),           # Assignment operator
    ('ID',       r'[A-Za-z]+'),   # Identifiers
    ('OP',       r'[+-*/]'),     # Arithmetic operators
    ('PRINT',    r'print'),       # print keyword
    ('SKIP',     r'[ \t]+'),      # Skip spaces and tabs
    ('MISMATCH', r'.'),           # Any other character
]

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        patterns = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECIFICATION)
        for mo in re.finditer(patterns, self.text):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)
            if kind != 'SKIP':
                self.tokens.append((kind, value))
