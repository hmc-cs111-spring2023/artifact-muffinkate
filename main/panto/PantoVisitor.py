from antlr4 import *
import turtle
import math
if __name__ is not None and "." in __name__:
    from .PantographParser import PantographParser
else:
    from PantographParser import PantographParser


class PantoVisitor(ParseTreeVisitor):
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.conversion_factor = 12
        self.s = turtle.Screen()
        self.t = turtle.Turtle()
        self.r = turtle.Turtle()
        self.spacing = 100
        self.curve = False
        self.radius = 100
        self.visited_first_node = False    

    def visitPanto(self , ctx): 
        self.s.screensize(self.screen_width, self.screen_height)
        self.s.setworldcoordinates(0, -(self.screen_height//2), self.screen_width, self.screen_height/2)
        self.t.penup()
        self.t.setposition(0,0)
        self.t.pendown()

        prop_rules = ctx.propagation()
        for r in prop_rules:
            self.visitOption(r.option(), self.t)

        design = ctx.line()
        for l in design:
            self.visitLine(l, self.t)
        
        self.r.penup
        self.r.pencolor("red")


        start_y = -(self.spacing)
        while start_y > -(self.screen_height//2):
            start_y = start_y - self.spacing

        for y in range(start_y, self.screen_height, self.spacing):
            self.visited_first_node = False
            self.r.penup()
            self.r.goto(0, y)
            if y != 0:
                self.r.seth(0)
                self.r.pendown()
                for l in design:
                    self.visitLine(l, self.r)

        self.s.exitonclick()
    
    def visitOption(self, ctx, t):
        o = ctx.getText().upper()
        
        if o.find("SCALE") != -1:
            s = self.visitArgument(ctx.getChild(0).argument())
            self.conversion_factor = self.conversion_factor * int(s)

        if o.find("SPACING") != -1:
            s = self.visitArgument(ctx.getChild(0).argument())
            self.spacing = int(s) * (self.screen_height // self.conversion_factor)
        
        if o.find("CURVE") != -1:
            self.curve = True
            r = self.visitArgument(ctx.getChild(0).argument())
            self.radius = self.conversion_factor * int(r)

    
    def visitLine(self, ctx, t):
        if self.curve != True:
            self.visitCommand(ctx.command(), t)
        else:
            self.visitCurveCommand(ctx.command(), t)

    def visitCommand(self, ctx, t):
        c = ctx.getText().upper()
        
        if c.find("DRAW") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())
            t.forward(int(n) * (self.screen_height // self.conversion_factor))
        
        if c.find("TURN") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())

            if c.find("LEFT") != -1:
                t.left(int(n))
            else:
                t.right(int(n))

    def visitCurveCommand(self, ctx, t):
        c = ctx.getText().upper()
        
        if c.find("DRAW") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())
            side = int(n) * (self.screen_height // self.conversion_factor)
            t.forward(side - (self.radius * 2))
        
        if c.find("TURN") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())

            if self.visited_first_node == False:
                if c.find("LEFT") != -1:
                    t.left(int(n))
                else:
                    t.right(int(n))
                self.visited_first_node = True
            elif c.find("LEFT") != -1:
                t.circle(self.radius, int(n))
            else:
                t.right(180)
                t.circle(self.radius, -int(n))
                t.right(180)


    def visitArgument(self, ctx):
        return ctx.NUMBER().getText()

