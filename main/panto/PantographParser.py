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
        4,1,14,85,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,0,4,0,38,8,0,11,0,12,0,
        39,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,55,8,
        3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,
        9,1,9,3,9,74,8,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,1,1,0,4,5,78,0,26,
        1,0,0,0,2,43,1,0,0,0,4,46,1,0,0,0,6,54,1,0,0,0,8,56,1,0,0,0,10,59,
        1,0,0,0,12,62,1,0,0,0,14,65,1,0,0,0,16,68,1,0,0,0,18,73,1,0,0,0,
        20,75,1,0,0,0,22,78,1,0,0,0,24,82,1,0,0,0,26,27,5,1,0,0,27,31,5,
        14,0,0,28,30,3,4,2,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,
        32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,6,0,0,35,37,5,14,
        0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,41,1,0,0,0,41,42,5,0,0,1,42,1,1,0,0,0,43,44,3,18,9,0,
        44,45,5,14,0,0,45,3,1,0,0,0,46,47,3,6,3,0,47,48,5,14,0,0,48,5,1,
        0,0,0,49,55,3,8,4,0,50,55,3,10,5,0,51,55,3,12,6,0,52,55,3,14,7,0,
        53,55,3,16,8,0,54,49,1,0,0,0,54,50,1,0,0,0,54,51,1,0,0,0,54,52,1,
        0,0,0,54,53,1,0,0,0,55,7,1,0,0,0,56,57,5,8,0,0,57,58,3,24,12,0,58,
        9,1,0,0,0,59,60,5,9,0,0,60,61,3,24,12,0,61,11,1,0,0,0,62,63,5,10,
        0,0,63,64,3,24,12,0,64,13,1,0,0,0,65,66,5,11,0,0,66,67,3,24,12,0,
        67,15,1,0,0,0,68,69,5,7,0,0,69,70,3,24,12,0,70,17,1,0,0,0,71,74,
        3,20,10,0,72,74,3,22,11,0,73,71,1,0,0,0,73,72,1,0,0,0,74,19,1,0,
        0,0,75,76,5,2,0,0,76,77,3,24,12,0,77,21,1,0,0,0,78,79,5,3,0,0,79,
        80,7,0,0,0,80,81,3,24,12,0,81,23,1,0,0,0,82,83,5,12,0,0,83,25,1,
        0,0,0,4,31,39,54,73
    ]

class PantographParser ( Parser ):

    grammarFileName = "Pantograph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PROPAGATE", "DRAW", "TURN", "LEFT", 
                      "RIGHT", "DESIGN", "SPACING", "OFFSET", "CURVE", "ROTATE", 
                      "SCALE", "NUMBER", "WHITESPACE", "NEWLINE" ]

    RULE_panto = 0
    RULE_line = 1
    RULE_propagation = 2
    RULE_option = 3
    RULE_offset = 4
    RULE_curve = 5
    RULE_rotate = 6
    RULE_scale = 7
    RULE_spacing = 8
    RULE_command = 9
    RULE_draw = 10
    RULE_turn = 11
    RULE_argument = 12

    ruleNames =  [ "panto", "line", "propagation", "option", "offset", "curve", 
                   "rotate", "scale", "spacing", "command", "draw", "turn", 
                   "argument" ]

    EOF = Token.EOF
    PROPAGATE=1
    DRAW=2
    TURN=3
    LEFT=4
    RIGHT=5
    DESIGN=6
    SPACING=7
    OFFSET=8
    CURVE=9
    ROTATE=10
    SCALE=11
    NUMBER=12
    WHITESPACE=13
    NEWLINE=14

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
            self.state = 26
            self.match(PantographParser.PROPAGATE)
            self.state = 27
            self.match(PantographParser.NEWLINE)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3968) != 0):
                self.state = 28
                self.propagation()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(PantographParser.DESIGN)
            self.state = 35
            self.match(PantographParser.NEWLINE)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.line()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==3):
                    break

            self.state = 41
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
            self.state = 43
            self.command()
            self.state = 44
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
            self.state = 46
            self.option()
            self.state = 47
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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 49
                self.offset()
                pass
            elif token in [9]:
                self.state = 50
                self.curve()
                pass
            elif token in [10]:
                self.state = 51
                self.rotate()
                pass
            elif token in [11]:
                self.state = 52
                self.scale()
                pass
            elif token in [7]:
                self.state = 53
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
            self.state = 56
            self.match(PantographParser.OFFSET)
            self.state = 57
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

        def argument(self):
            return self.getTypedRuleContext(PantographParser.ArgumentContext,0)


        def getRuleIndex(self):
            return PantographParser.RULE_curve




    def curve(self):

        localctx = PantographParser.CurveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_curve)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(PantographParser.CURVE)
            self.state = 60
            self.argument()
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
        self.enterRule(localctx, 12, self.RULE_rotate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(PantographParser.ROTATE)
            self.state = 63
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
        self.enterRule(localctx, 14, self.RULE_scale)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(PantographParser.SCALE)
            self.state = 66
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
        self.enterRule(localctx, 16, self.RULE_spacing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PantographParser.SPACING)
            self.state = 69
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
        self.enterRule(localctx, 18, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 71
                self.draw()
                pass
            elif token in [3]:
                self.state = 72
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
        self.enterRule(localctx, 20, self.RULE_draw)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PantographParser.DRAW)
            self.state = 76
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
        self.enterRule(localctx, 22, self.RULE_turn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(PantographParser.TURN)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 80
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
        self.enterRule(localctx, 24, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(PantographParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





