import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(another_turtle):
    for i in range(1,4):
        another_turtle.forward(50)
        another_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.setup (width=.5, height=.5)
    window.bgcolor("yellow")
    # defines brad the turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black", "green")
    brad.speed(10)
    # gets brad to draw the square 
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    # defines angle the turtle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    # gets angie to draw a circle
    angie.circle(80)
    # defines marie the turtle
    marie = turtle.Turtle()
    marie.color("red")
    # gets marie to draw the traingle
    draw_triangle(marie)
    
    window.exitonclick()

draw_art()
