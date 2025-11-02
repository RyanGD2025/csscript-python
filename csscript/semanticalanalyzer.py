from ast import *

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, nodes):
        for node in nodes:
            self.visit(node)

    def visit(self, node):
        if isinstance(node, Assign):
            value = self.eval_expr(node.expr)
            self.symbol_table[node.name] = value
        elif isinstance(node, Print):
            value = self.eval_expr(node.expr)
            print(value)
        else:
            raise Exception("Unsupported node")

    def eval_expr(self, node):
        if isinstance(node, Num):
            return node.value
        elif isinstance(node, Var):
            if node.name in self.symbol_table:
                return self.symbol_table[node.name]
            else:
                raise Exception(f"Undefined variable '{node.name}'")
        elif isinstance(node, BinOp):
            left = self.eval_expr(node.left)
            right = self.eval_expr(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
        else:
            raise Exception("Invalid expression")
