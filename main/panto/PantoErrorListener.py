from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class PantoErrorListener(ErrorListener):
    """
    taken from https://stackoverflow.com/questions/18132078/handling-errors-in-antlr4
    """
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ex = ParseCancellationException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        raise ex