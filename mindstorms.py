import turtle


window = turtle.Screen()
window.setup (width=.5, height=.5)
window.bgcolor("yellow")

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black", "green")
    brad.speed(1)
    n = 0

    while (n<4):
        brad.forward(100)
        brad.right(90)
        n = n + 1

    else:
        quit

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    marie = turtle.Turtle()
    marie.color("purple")
    n = 0

    while (n<3):
        marie.forward(50)
        marie.left(120)
        n = n + 1

    else:
        quit
    
    window.exitonclick()

draw_square()

draw_circle()

draw_triangle()
