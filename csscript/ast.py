class Node:
    pass

class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(Node):
    def __init__(self, value):
        self.value = value

class Var(Node):
    def __init__(self, name):
        self.name = name

class Assign(Node):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class Print(Node):
    def __init__(self, expr):
        self.expr = expr
