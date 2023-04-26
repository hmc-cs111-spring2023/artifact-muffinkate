# Generated from Pantograph.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,0,4,
        0,42,8,0,11,0,12,0,43,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,3,3,59,8,3,1,4,1,4,1,4,1,5,1,5,1,5,3,5,67,8,5,1,6,1,6,
        1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,3,11,84,
        8,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,0,0,15,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,1,1,0,4,5,87,0,30,1,0,0,
        0,2,47,1,0,0,0,4,50,1,0,0,0,6,58,1,0,0,0,8,60,1,0,0,0,10,63,1,0,
        0,0,12,68,1,0,0,0,14,70,1,0,0,0,16,72,1,0,0,0,18,75,1,0,0,0,20,78,
        1,0,0,0,22,83,1,0,0,0,24,85,1,0,0,0,26,88,1,0,0,0,28,92,1,0,0,0,
        30,31,5,1,0,0,31,35,5,16,0,0,32,34,3,4,2,0,33,32,1,0,0,0,34,37,1,
        0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,
        39,5,8,0,0,39,41,5,16,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,43,1,0,
        0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,0,0,1,46,1,
        1,0,0,0,47,48,3,22,11,0,48,49,5,16,0,0,49,3,1,0,0,0,50,51,3,6,3,
        0,51,52,5,16,0,0,52,5,1,0,0,0,53,59,3,8,4,0,54,59,3,10,5,0,55,59,
        3,16,8,0,56,59,3,18,9,0,57,59,3,20,10,0,58,53,1,0,0,0,58,54,1,0,
        0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,7,1,0,0,0,60,61,
        5,10,0,0,61,62,3,28,14,0,62,9,1,0,0,0,63,66,5,11,0,0,64,67,3,12,
        6,0,65,67,3,14,7,0,66,64,1,0,0,0,66,65,1,0,0,0,67,11,1,0,0,0,68,
        69,5,6,0,0,69,13,1,0,0,0,70,71,5,7,0,0,71,15,1,0,0,0,72,73,5,12,
        0,0,73,74,3,28,14,0,74,17,1,0,0,0,75,76,5,13,0,0,76,77,3,28,14,0,
        77,19,1,0,0,0,78,79,5,9,0,0,79,80,3,28,14,0,80,21,1,0,0,0,81,84,
        3,24,12,0,82,84,3,26,13,0,83,81,1,0,0,0,83,82,1,0,0,0,84,23,1,0,
        0,0,85,86,5,2,0,0,86,87,3,28,14,0,87,25,1,0,0,0,88,89,5,3,0,0,89,
        90,7,0,0,0,90,91,3,28,14,0,91,27,1,0,0,0,92,93,5,14,0,0,93,29,1,
        0,0,0,5,35,43,58,66,83
    ]

class PantographParser ( Parser ):

    grammarFileName = "Pantograph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PROPAGATE", "DRAW", "TURN", "LEFT", 
                      "RIGHT", "TRUE", "FALSE", "DESIGN", "SPACING", "OFFSET", 
                      "CURVE", "ROTATE", "SCALE", "NUMBER", "WHITESPACE", 
                      "NEWLINE" ]

    RULE_panto = 0
    RULE_line = 1
    RULE_propagation = 2
    RULE_option = 3
    RULE_offset = 4
    RULE_curve = 5
    RULE_true = 6
    RULE_false = 7
    RULE_rotate = 8
    RULE_scale = 9
    RULE_spacing = 10
    RULE_command = 11
    RULE_draw = 12
    RULE_turn = 13
    RULE_argument = 14

    ruleNames =  [ "panto", "line", "propagation", "option", "offset", "curve", 
                   "true", "false", "rotate", "scale", "spacing", "command", 
                   "draw", "turn", "argument" ]

    EOF = Token.EOF
    PROPAGATE=1
    DRAW=2
    TURN=3
    LEFT=4
    RIGHT=5
    TRUE=6
    FALSE=7
    DESIGN=8
    SPACING=9
    OFFSET=10
    CURVE=11
    ROTATE=12
    SCALE=13
    NUMBER=14
    WHITESPACE=15
    NEWLINE=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPAGATE(self):
            return self.getToken(PantographParser.PROPAGATE, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PantographParser.NEWLINE)
            else:
                return self.getToken(PantographParser.NEWLINE, i)

        def DESIGN(self):
            return self.getToken(PantographParser.DESIGN, 0)

        def EOF(self):
            return self.getToken(PantographParser.EOF, 0)

        def propagation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PantographParser.PropagationContext)
            else:
                return self.getTypedRuleContext(PantographParser.PropagationContext,i)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PantographParser.LineContext)
            else:
                return self.getTypedRuleContext(PantographParser.LineContext,i)


        def getRuleIndex(self):
            return PantographParser.RULE_panto




    def panto(self):

        localctx = PantographParser.PantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_panto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(PantographParser.PROPAGATE)
            self.state = 31
            self.match(PantographParser.NEWLINE)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0):
                self.state = 32
                self.propagation()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(PantographParser.DESIGN)
            self.state = 39
            self.match(PantographParser.NEWLINE)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.line()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==3):
                    break

            self.state = 45
            self.match(PantographParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(PantographParser.CommandContext,0)


        def NEWLINE(self):
            return self.getToken(PantographParser.NEWLINE, 0)

        def getRuleIndex(self):
            return PantographParser.RULE_line




    def line(self):

        localctx = PantographParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.command()
            self.state = 48
            self.match(PantographParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropagationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option(self):
            return self.getTypedRuleContext(PantographParser.OptionContext,0)


        def NEWLINE(self):
            return self.getToken(PantographParser.NEWLINE, 0)

        def getRuleIndex(self):
            return PantographParser.RULE_propagation




    def propagation(self):

        localctx = PantographParser.PropagationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_propagation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.option()
            self.state = 51
            self.match(PantographParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def offset(self):
            return self.getTypedRuleContext(PantographParser.OffsetContext,0)


        def curve(self):
            return self.getTypedRuleContext(PantographParser.CurveContext,0)


        def rotate(self):
            return self.getTypedRuleContext(PantographParser.RotateContext,0)


        def scale(self):
            return self.getTypedRuleContext(PantographParser.ScaleContext,0)


        def spacing(self):
            return self.getTypedRuleContext(PantographParser.SpacingContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_option




    def option(self):

        localctx = PantographParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 53
                self.offset()
                pass
            elif token in [11]:
                self.state = 54
                self.curve()
                pass
            elif token in [12]:
                self.state = 55
                self.rotate()
                pass
            elif token in [13]:
                self.state = 56
                self.scale()
                pass
            elif token in [9]:
                self.state = 57
                self.spacing()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OffsetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OFFSET(self):
            return self.getToken(PantographParser.OFFSET, 0)

        def argument(self):
            return self.getTypedRuleContext(PantographParser.ArgumentContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_offset




    def offset(self):

        localctx = PantographParser.OffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_offset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(PantographParser.OFFSET)
            self.state = 61
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CurveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURVE(self):
            return self.getToken(PantographParser.CURVE, 0)

        def true(self):
            return self.getTypedRuleContext(PantographParser.TrueContext,0)


        def false(self):
            return self.getTypedRuleContext(PantographParser.FalseContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_curve




    def curve(self):

        localctx = PantographParser.CurveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_curve)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(PantographParser.CURVE)
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 64
                self.true()
                pass
            elif token in [7]:
                self.state = 65
                self.false()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(PantographParser.TRUE, 0)

        def getRuleIndex(self):
            return PantographParser.RULE_true




    def true(self):

        localctx = PantographParser.TrueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_true)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PantographParser.TRUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FalseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FALSE(self):
            return self.getToken(PantographParser.FALSE, 0)

        def getRuleIndex(self):
            return PantographParser.RULE_false




    def false(self):

        localctx = PantographParser.FalseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_false)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(PantographParser.FALSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RotateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROTATE(self):
            return self.getToken(PantographParser.ROTATE, 0)

        def argument(self):
            return self.getTypedRuleContext(PantographParser.ArgumentContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_rotate




    def rotate(self):

        localctx = PantographParser.RotateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rotate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(PantographParser.ROTATE)
            self.state = 73
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScaleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCALE(self):
            return self.getToken(PantographParser.SCALE, 0)

        def argument(self):
            return self.getTypedRuleContext(PantographParser.ArgumentContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_scale




    def scale(self):

        localctx = PantographParser.ScaleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_scale)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PantographParser.SCALE)
            self.state = 76
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpacingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACING(self):
            return self.getToken(PantographParser.SPACING, 0)

        def argument(self):
            return self.getTypedRuleContext(PantographParser.ArgumentContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_spacing




    def spacing(self):

        localctx = PantographParser.SpacingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_spacing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(PantographParser.SPACING)
            self.state = 79
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def draw(self):
            return self.getTypedRuleContext(PantographParser.DrawContext,0)


        def turn(self):
            return self.getTypedRuleContext(PantographParser.TurnContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_command




    def command(self):

        localctx = PantographParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 81
                self.draw()
                pass
            elif token in [3]:
                self.state = 82
                self.turn()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DrawContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRAW(self):
            return self.getToken(PantographParser.DRAW, 0)

        def argument(self):
            return self.getTypedRuleContext(PantographParser.ArgumentContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_draw




    def draw(self):

        localctx = PantographParser.DrawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_draw)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(PantographParser.DRAW)
            self.state = 86
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TurnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TURN(self):
            return self.getToken(PantographParser.TURN, 0)

        def argument(self):
            return self.getTypedRuleContext(PantographParser.ArgumentContext,0)


        def LEFT(self):
            return self.getToken(PantographParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(PantographParser.RIGHT, 0)

        def getRuleIndex(self):
            return PantographParser.RULE_turn




    def turn(self):

        localctx = PantographParser.TurnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_turn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(PantographParser.TURN)
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 90
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PantographParser.NUMBER, 0)

        def getRuleIndex(self):
            return PantographParser.RULE_argument




    def argument(self):

        localctx = PantographParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(PantographParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





