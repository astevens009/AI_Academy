# Exercise: Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
#       An equilateral triangle
#       A square
#       A hexagon (six sides)
#       An octagon (eight sides)

import turtle

def draw_polygon(t, sideLength, numSides):
    turn_angle = 360 / numSides
    for sides in range(numSides):
        t.forward(sideLength)
        t.left(turn_angle)

def move_turtle(t: turtle, x_coord: float, y_coord: float):
    """Move the turtle to desiganted coordinates before drawing

    Args:
        t (turtle): The turtle object
        x_coord (float): The x-coordinate of the screen
        y_coord (float): the y-coordinate of the screen

    Returns:
        None: None
    """
    t.penup()
    t.goto(x_coord, y_coord)
    t.pendown()
    # return t


win = turtle.Screen()
win.bgcolor("black")

polly = turtle.Turtle()
polly.shape("turtle")
polly.color("gold")
polly.pensize(8)

# Triangle
draw_polygon(polly, 200, 3)

# Square
move_turtle(polly, -200, 0)
polly.color("firebrick")
draw_polygon(polly, 200, 4)

# Hexagon
move_turtle(polly, -200, -250)
polly.color("forestgreen")
draw_polygon(polly, 150, 6)

# Octagon
move_turtle(polly, -350, 150)
polly.color("purple")
draw_polygon(polly, 150, 8)

win.exitonclick()
