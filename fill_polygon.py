import turtle
win = turtle.Screen()
win.bgcolor("black")

def draw_polygon(t, sideLength, numSides):
    turn_angle = 360 / numSides
    
    for sides in range(numSides):
        t.forward(sideLength)
        t.left(turn_angle)
    

def draw_fill_polygon(t, numSides, sideLength, shapeCol):
    turn_angle = 360 / numSides
    t.fillcolor(shapeCol)

    t.begin_fill()
    for sides in range(numSides):
        t.forward(sideLength)
        t.left(turn_angle)
    t.end_fill()

# Create the turtle object
polly = turtle.Turtle()
polly.shape("turtle")
polly.color("gold")
polly.pensize(8)

# Prompt user for information
num_of_sides = int(input("Please enter the number of sides for the shape: "))
side_length = int(input("Please enter the length of the side: "))
shape_color = input("Please choose a color: ")

# Triangle
draw_fill_polygon(polly, num_of_sides, side_length, shape_color)

win.exitonclick()