import sys
from antlr4 import *
from PantographLexer import PantographLexer
from PantographParser import PantographParser
from PyPantographListener import PyPantographListener

def main(argv):
    input = FileStream(argv[1])
    lexer = PantographLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PantographParser(stream)
    tree = parser.chat()

    output = open("output.html","w")
    
    panto = PyPantographListener(output)
    walker = ParseTreeWalker()
    walker.walk(panto, tree)
        
    output.close()      

if __name__ == '__main__':
    main(sys.argv)