from antlr4 import *
import turtle
import math
from PantoUtil import *
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
    curve               : a value to say whether the line is straight, 
                        slightly curved, or completely curved. Default is
                        "None" which indicates a straight line. "Low"
                        indicates a curve_percent of 25, with curved corners,
                        and "High" indicates the whole-curve design using
                        the point traversal methods.
    curve_percent       : the percent of the each line in the design that
                        becomes part of the curved corner. Default is 0.
    old_side            : an attribute used only if curve is low to track
                        the length of the previous straight line
    midpoint            : an attribute used only if curve is high to track
                        the midpoint of the current side being curved from.
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
    curvedCorners
    sharpCorners
    curveDesign

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
        self.curve = "None"
        self.midpoint = (0,0)
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
            self.visitOption(r.option())

        if self.curve == "High":
            self.curvedCorners(ctx)
        else:
            self.sharpCorners(ctx)

        self.s.exitonclick()

    def curvedCorners(self, ctx):
        """ Creates a line that is bounded by the same points as sharpCorners,
        but curves the corners. First traverses the parse tree to return all
        the points, then uses that to draw the appropriate lines."""

        # visit the parse tree and return the boundary points
        # "boundary points" are the points from the unmodified design that
        # the turtle turns at, and are the targets for the curved lines
        points = []
        design = ctx.line()
        self.t.penup()
        self.t.ht()
        self.t.speed(0)

        for l in design:
            points.append(self.getPoint(l, self.t))

        # reset turtle's speed and position
        self.t.showturtle()
        #self.t.speed('fast')
        self.t.setpos(0,0)
        self.t.pendown()

        # first design
        self.curveDesign(points, self.t)

        # warning message that entrance/exit points are not the same
        if self.t.ycor() != 0:
            print("WARNING: Entrance and exit points are not the same")

        # sets up the propagation turtle
        self.r.penup()
        self.r.pencolor("red")
        self.r.speed(0)

        # horizontal propagation
        self.r.setpos(self.t.pos())
        while self.r.xcor() <= self.screen_width:
            points_temp = update_points(points, self.r.pos())
            self.r.seth(0)
            self.r.pendown()
            self.curveDesign(points_temp, self.r)
        self.r.penup()

        # vertical propogation
        # calculate the starting y postition based on the spacing
        start_y = -(self.spacing)
        while start_y > -(self.screen_height//2):
            start_y = start_y - self.spacing

        # vertically propagate
        for y in range(start_y, self.screen_height, self.spacing):
            self.visited_first_node = False
            self.r.penup()
            self.r.goto(0, y)
            if y != 0:
                while self.r.xcor() <= self.screen_width:
                    points_temp = update_points(points, self.r.pos())
                    self.r.seth(0)
                    self.r.pendown()
                    self.curveDesign(points_temp, self.r)


    def curveDesign(self, points, t):
        """
        Draws the curved design using the list of points from
        the straight-edge version, and the given turtle
        """
        for i in range(0, len(points)):
            p0 = points[i][0]
            p1 = points[i][1]
            # if it's a turn, arc to the appropriate point in the next pair
            if p0 == p1:
                next_point = points[i+1]
                next_midpoint = ((next_point[1][0] + next_point[0][0])/2, (next_point[1][1] + next_point[0][1])/2)
                new_x = next_midpoint[0]-self.midpoint[0]
                new_y = next_midpoint[1]-self.midpoint[1]
                toggle = turn_toggle(new_x, new_y, t.heading())
                if toggle:
                    arc(new_x, -1*new_y, t.xcor(), t.ycor(), t)
                else:
                    t.penup()
                    t.goto(next_midpoint)
                    t.pendown()
                    arc(-1*new_x, new_y, t.xcor(), t.ycor(), t)
                    t.penup()
                    t.goto(next_midpoint)
                    t.pendown()
                    t.left(180)

            # if it's a draw command, move forward the appropriate amount
            else:
                self.midpoint = ((p0[0] + p1[0])/2, (p0[1] + p1[1])/2)
                t.goto(self.midpoint)


    def getPoint(self, ctx, t):
        return self.getCommandPoint(ctx.command(), t)

    def sharpCorners(self, ctx):
        """ Visits each node directly as written, with all straight lines
        and sharp corners"""

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

        # vertically propagate
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


    def visitOption(self, ctx):
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
            p = ctx.getChild(0).getText().upper()
            if p.find("LOW") != -1:
                self.curve = "Low"
            self.curve_percent = "High"
                

    
    def visitLine(self, ctx, t):
        """ Visits a command node, and calls VisitCommand
        if curve is false, and calls VisitCurveCommand if
        the design is supposed to be curved """
        if self.curve != "Low":
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
        curve = 25

        if c.find("DRAW") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())
            side = int(n) * (self.screen_height // self.conversion_factor)
            t.forward(((100 - curve) * side) // 100)
            self.old_side = side

        if c.find("TURN") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())
            radius = (curve * self.old_side) // 100

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
    
    def getCommandPoint(self, ctx, t):
        """ Returns the point of the turtle post-command in the
         straight design """
        c = ctx.getText().upper()
        old_pos = t.position()
        new_pos = (0,0)
        if c.find("DRAW") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())
            t.forward(int(n) * (self.screen_height // self.conversion_factor))
            new_pos = t.position()
        
        if c.find("TURN") != -1:
            n = self.visitArgument(ctx.getChild(0).argument())
            if c.find("LEFT") != -1:
                t.left(int(n))
            else:
                t.right(int(n))
            new_pos = t.position()
        return (old_pos, new_pos)

 
    def visitArgument(self, ctx):
        """ Returns an argument as a string """
        return ctx.NUMBER().getText()
    
