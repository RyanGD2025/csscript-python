from lexer import Lexer
from parser import Parser
from semanticalanalyzer import SemanticAnalyzer

def run_code(code):
    lexer = Lexer(code)
    parser = Parser(lexer.tokens)
    nodes = parser.parse()
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.analyze(nodes)

if __name__ == "__main__":
    sample_code = """
    x = 10
    y = 5
    print x + y
    z = x * y
    print z
    """
    run_code(sample_code)
