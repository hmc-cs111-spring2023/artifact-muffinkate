import turtle
import math

def arc(wid, ht, start_x, start_y, turble):
    """ Draws an arc by drawing a quarter of an ellipse
        given a width and a height
    """
    for i in range(91):
        t = i * (math.pi / 180)
        x = start_x + (wid * math.sin(t))
        y = start_y + (ht * math.cos(t) - ht)
        turble.setheading(turble.towards(x, y))
        turble.goto(x,y)

def turn_toggle(x, y, heading):
    """
        Determines whether the turtle needs to negate the
        y-direction or not

        Quadrants are determined in relation to what point the
        turtle currently is at

        Returns a boolean
    """
    # turtle is heading in the first quadrant
    if heading >= 0 and heading < 90:
        if x < 0 and y > 0:
            return False
        return True
    # turtle is heading in the second quadrant
    elif heading >= 90 and heading < 180:
        if x > 0 and y > 0:
            return False
        return True
    # turtle is heading in the third quadrant
    elif heading >= 180 and heading < 270:
        if x > 0 and y < 0:
            return False
        return True
    # turtle is heading in the fourth quadrant
    elif heading >= 270 and heading < 360:
        if x < 0 and y < 0:
            return False
        return True
    return True

def update_points(points, new_home):
    """ Creates a temporary list of points, updated by
    where the turtle has last ended. """
    new_points = []
    new_x = new_home[0]
    new_y = new_home[1]
    for point_pair in points:
        p0 = (point_pair[0][0] + new_x, point_pair[0][1] + new_y)
        p1 = (point_pair[1][0] + new_x, point_pair[1][1] + new_y)
        new_points.append((p0, p1))
    return new_points

