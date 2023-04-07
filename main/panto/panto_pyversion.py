import turtle
import math

# things for setting up screen, regardless of code
screen_width = 500
screen_height = 500

s = turtle.Screen()
t = turtle.Turtle()
s.screensize(screen_width, screen_height)
s.setworldcoordinates(0, -(screen_height//2), screen_width, screen_height/2)
t.getscreen()
t.penup()
t.setposition(0,0)
t.pendown()

# user written code
def design(t):
    t.left(45)
    t.forward((screen_width / 4) / math.cos(math.radians(45)))

    t.right(90)
    t.forward((screen_width / 2) / math.cos(math.radians(45)))

    t.left(90)
    t.forward((screen_width / 4) / math.cos(math.radians(45)))

design(t)

# propogation
spacing = 100

r = turtle.Turtle()
r.penup
r.pencolor("red")
for y in range(-(screen_height//2)-50, screen_height, spacing):
    r.penup()
    r.goto(0, y)
    if y != 0:
        r.seth(0)
        r.pendown()
        design(r)



# end of program - workshop as api develops
turtle.Screen().exitonclick() 
