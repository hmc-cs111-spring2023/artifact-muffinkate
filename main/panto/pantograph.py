import sys
from antlr4 import *
from PantographLexer import PantographLexer
from PantographParser import PantographParser
from PantoVisitor import PantoVisitor

def main(argv):
    input = FileStream(argv[1])
    lexer = PantographLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PantographParser(stream)
    visitor = ParseTreeVisitor()
    tree = parser.panto()
    
    panto = PantoVisitor(visitor)
    walker = ParseTreeWalker()
    walker.walk(panto, tree)     

if __name__ == '__main__':
    main(sys.argv)