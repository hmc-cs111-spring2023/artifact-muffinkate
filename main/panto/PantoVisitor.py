from antlr4 import *
import turtle
import math
if __name__ is not None and "." in __name__:
    from .PantographParser import PantographParser
else:
    from PantographParser import PantographParser


class PantoVisitor(ParseTreeVisitor):
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.s = turtle.Screen()
        self.t = turtle.Turtle()
        self.r = turtle.Turtle()
        self.spacing = 100
    

    def visitPanto(self , ctx): 
        self.s.screensize(self.screen_width, self.screen_height)
        self.s.setworldcoordinates(0, -(self.screen_height//2), self.screen_width, self.screen_height/2)
        self.t.penup()
        self.t.setposition(0,0)
        self.t.pendown()

        prop_rules = ctx.propogation()
        for r in prop_rules:
            self.visit(r)

        design = ctx.line()
        for l in design:
            self.visitLine(l, self.t)
        
        self.r.penup
        self.r.pencolor("red")

        for y in range(-(self.screen_height//2)-50, self.screen_height, self.spacing):
            self.r.penup()
            self.r.goto(0, y)
            if y != 0:
                self.r.seth(0)
                self.r.pendown()
                for l in design:
                    self.visitLine(l, self.r)

        self.s.exitonclick()
    
    def visitLine(self, ctx, t):
        self.visitCommand(ctx.command(), t)

    def visitCommand(self, ctx, t):
        c = ctx.getText().upper()
        
        if c.find("DRAW") != -1:
            n = self.visit(ctx.getChild(0).argument())
            t.forward(int(n))
        
        if c.find("TURN") != -1:
            n = self.visit(ctx.getChild(0).argument())

            if c.find("LEFT") != -1:
                t.left(int(n))
            else:
                t.right(int(n))

    def visitArgument(self, ctx):
        return ctx.NUMBER().getText()
