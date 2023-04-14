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

def swirl(t):
    t.forward(50)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20) 
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20) 
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)

def design(t):
    while t.xcor() < screen_width:
        swirl(t)

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

turtle.Screen().exitonclick() 