import sys
from antlr4 import *
from PantographParser import PantographParser
from PantographListener import PantographListener

class PyPantographListener(PantographListener) :
    def __init__(self, output):
        self.output = output
        self.output.write('<html><head><meta charset="UTF-8"/></head><body>')

    # Enter a parse tree produced by PantographParser#panto.
    def enterPanto(self, ctx:PantographParser.PantoContext):
        pass

    # Exit a parse tree produced by PantographParser#panto.
    def exitPanto(self, ctx:PantographParser.PantoContext):
        pass


    # Enter a parse tree produced by PantographParser#line.
    def enterLine(self, ctx:PantographParser.LineContext):
        pass

    # Exit a parse tree produced by PantographParser#line.
    def exitLine(self, ctx:PantographParser.LineContext):
        pass


    # Enter a parse tree produced by PantographParser#propogation.
    def enterPropogation(self, ctx:PantographParser.PropogationContext):
        pass

    # Exit a parse tree produced by PantographParser#propogation.
    def exitPropogation(self, ctx:PantographParser.PropogationContext):
        pass


    # Enter a parse tree produced by PantographParser#command.
    def enterCommand(self, ctx:PantographParser.CommandContext):
        pass

    # Exit a parse tree produced by PantographParser#command.
    def exitCommand(self, ctx:PantographParser.CommandContext):
        pass


    # Enter a parse tree produced by PantographParser#draw.
    def enterDraw(self, ctx:PantographParser.DrawContext):
        pass

    # Exit a parse tree produced by PantographParser#draw.
    def exitDraw(self, ctx:PantographParser.DrawContext):
        pass


    # Enter a parse tree produced by PantographParser#turn.
    def enterTurn(self, ctx:PantographParser.TurnContext):
        pass

    # Exit a parse tree produced by PantographParser#turn.
    def exitTurn(self, ctx:PantographParser.TurnContext):
        pass


    # Enter a parse tree produced by PantographParser#argument.
    def enterArgument(self, ctx:PantographParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PantographParser#argument.
    def exitArgument(self, ctx:PantographParser.ArgumentContext):
        pass

    
    def enterName(self, ctx:PantographParser.NameContext) :
        self.output.write("<strong>") 

    def exitName(self, ctx:PantographParser.NameContext) :
        self.output.write(ctx.WORD().getText()) 
        self.output.write("</strong> ") 

    def enterColor(self, ctx:PantographParser.ColorContext) :
        color = ctx.WORD().getText()
        ctx.text = '<span style="color: ' + color + '">'        

    def exitColor(self, ctx:PantographParser.ColorContext):         
        ctx.text += ctx.message().text
        ctx.text += '</span>'

    def exitEmoticon(self, ctx:PantographParser.EmoticonContext) : 
        emoticon = ctx.getText()

        if emoticon == ':-)' or emoticon == ':)' :
            ctx.text = "🙂"
    
        if emoticon == ':-(' or emoticon == ':(' :
            ctx.text = "🙁"

    def enterLink(self, ctx:PantographParser.LinkContext):
        ctx.text = '<a href="%s">%s</a>' % (ctx.TEXT()[1], (ctx.TEXT()[0]))

    def exitMessage(self, ctx:PantographParser.MessageContext):
        text = ''

        for child in ctx.children:
            if hasattr(child, 'text'):
                text += child.text
            else:
                text += child.getText()
        
        if isinstance(ctx.parentCtx, PantographParser.LineContext) is False:
            ctx.text = text
        else:    
            self.output.write(text)
            self.output.write("</p>") 

    def enterCommand(self, ctx:PantographParser.CommandContext):
        if ctx.SAYS() is not None :
            self.output.write(ctx.SAYS().getText() + ':' + '<p>')

        if ctx.SHOUTS() is not None :
            self.output.write(ctx.SHOUTS().getText() + ':' + '<p style="text-transform: uppercase">')    

    def exitChat(self, ctx:PantographParser.ChatContext):
        self.output.write("</body></html>")