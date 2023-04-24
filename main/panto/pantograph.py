import sys
from antlr4 import *
from PantographLexer import PantographLexer
from PantographParser import PantographParser
from PantoVisitor import PantoVisitor
from PantoErrorListener import PantoErrorListener

def main(argv):
    input = FileStream(argv[1])
    lexer = PantographLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(PantoErrorListener())

    stream = CommonTokenStream(lexer)
    parser = PantographParser(stream)
    tree = parser.panto()
    # print(tree.toStringTree())
    panto = PantoVisitor()
    parser.removeErrorListeners()
    parser.addErrorListener(PantoErrorListener())

    panto.visitPanto(tree)    

if __name__ == '__main__':
    main(sys.argv)