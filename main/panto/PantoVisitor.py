from antlr4 import *
import turtle
import math
if __name__ is not None and "." in __name__:
    from .PantographParser import PantographParser
else:
    from PantographParser import PantographParser


class PantoVisitor(ParseTreeVisitor):
    """
    This class defines a visitor for a parse tree created by PantographParser for a
    program written in the Pantograph DSL.
    
    Attributes:
    screen_width        : the width in pixels of the turtle screen, 600
    screen_height       : the height in pixels of the turtle screen, 60
    conversion_factor   : the number to convert the arguments, given in inches
                        or feet, into pixels. It changes depending on the
                        scale of the screen, but default is 12
    s                   : the turtle screen object
    t                   : the turtle object for the original line design
    r                   : the turtle object for the copied designs
    spacing             : the number, in pixels, that vertically separates
                        each line of the design. Default is 100 pixels.
    curve               : a boolean to say if the design is curved or not
                        to trigger which function it uses for each node.
                        Default is false.
    curve_percent       : the percent of the each line in the design that
                        becomes part of the curved corner. Default is 0.
    old_side            : an attribute used only if curve is true to track
                        the length of the most recent side that was drawn.
    visited_first_node  : boolean to track whether the first node has been
                        visited, so that if it curves and turns first in 
                        the design, it turns in place.

    Methods:
    visitPanto
    visitOption
    visitLine
    visitCommand
    visitCurveCommand
    visitArgument

    """
    def __init__(self):
        # set the default screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.conversion_factor = 12
        self.s = turtle.Screen()
        self.t = turtle.Turtle() 
        self.r = turtle.Turtle() 
        self.spacing = 100
        self.curve = False
        self.curve_percent = 0
        self.old_side = 0
        self.visited_first_node = False    

    def visitPanto(self , ctx): 
        """ Visits the topmost node, Panto, creates a screen and visits
        the children nodes to draw and propagate the design
        """
        # create the screen and turtle
        self.s.screensize(self.screen_width, self.screen_height)
        self.s.setworldcoordinates(0, -(self.screen_height//2), self.screen_width, self.screen_height/2)
        self.t.penup()
        self.t.setposition(0,0)
        self.t.pendown()

        # visit the propagation rules from the parse tree
        prop_rules = ctx.propagation()
        for r in prop_rules:
            self.visitOption(r.option(), self.t)

        # visit the design rules from the parse tree
        design = ctx.line()
        for l in design:
            self.visitLine(l, self.t)
        
        # warning message that entrance/exit points are not the same
        if self.t.ycor() != 0:
            print("WARNING: Entrance and exit points are not the same")

        # sets up the propagation turtle
        self.r.penup()
        self.r.pencolor("red")

        # horizontal propagation
        self.r.setpos(self.t.pos())
        while self.r.xcor() <= self.screen_width:
            self.r.seth(0)
            self.r.pendown()
            for l in design:
                self.visitLine(l, self.r)
        self.r.penup()

        # calculate the starting y postition based on the spacing
        start_y = -(self.spacing)
        while start_y > -(self.screen_height//2):
            start_y = start_y - self.spacing

        # vertically propagation
        for y in range(start_y, self.screen_height, self.spacing):
            self.visited_first_node = False
            self.r.penup()
            self.r.goto(0, y)
            if y != 0:
                while self.r.xcor() <= self.screen_width:
                    self.r.seth(0)
                    self.r.pendown()
                    for l in design:
                        self.visitLine(l, self.r)

        self.s.exitonclick()
    
    def visitOption(self, ctx, t):
        """ Each option node is a propagation setting. This gets
        all the arguments and assigns them to the appropriate settings"""
        o = ctx.getText().upper()
        
        if o.find("SCALE") != -1:
            s = self.visitArgument(ctx.getChild(0).argument())
            self.conversion_factor = self.conversion_factor * int(s)

        if o.find("SPACING") != -1:
            s = self.visitArgument(ctx.getChild(0).argument())
            self.spacing = int(s) * (self.screen_height // self.conversion_factor)
        
        if o.find("CURVE") != -1:
            self.curve = True
            p = int(self.visitArgument(ctx.getChild(0).argument()))
            if p != 0:
                self.curve_percent = int(p)
            else:
                self.curve = False

    
    def visitLine(self, ctx, t):
        """ Visits a command node, and calls VisitCommand
        if curve is false, and calls VisitCurveCommand if
        the design is supposed to be curved """
        if self.curve != True or self.curve_percent == 0:
            self.visitCommand(ctx.command(), t)
        else:
            self.visitCurveCommand(ctx.command(), t)

    def visitCommand(self, ctx, t):
        """" Moves or turns the turtle depending on the argument """
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
        """ Moves or turns the turtle depending on the argument """
        c = ctx.getText().upper()
        
        if c.find("DRAW") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())
            side = int(n) * (self.screen_height // self.conversion_factor)
            t.forward(((100 - self.curve_percent) * side) // 100)
            self.old_side = side
        
        if c.find("TURN") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())
            radius = (self.curve_percent * self.old_side) // 100

            if self.visited_first_node == False:
                if c.find("LEFT") != -1:
                    t.left(int(n))
                else:
                    t.right(int(n))
                self.visited_first_node = True
            elif c.find("LEFT") != -1:
                t.circle(radius, int(n))
            else:
                t.right(180)
                t.circle(radius, -int(n))
                t.right(180)


    def visitArgument(self, ctx):
        """ Returns an argument as a string """
        return ctx.NUMBER().getText()

