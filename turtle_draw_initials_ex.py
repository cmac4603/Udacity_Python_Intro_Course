import turtle

def draw_c(some_turtle):
    some_turtle.right(180)
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100)

def draw_m(another_turtle):
    another_turtle.left(90)
    another_turtle.forward(100)
    another_turtle.right(135)
    another_turtle.forward(100)
    another_turtle.left(90)
    another_turtle.forward(100)
    another_turtle.right(135)
    another_turtle.forward(100)

def draw_initials():
    window = turtle.Screen()
    window.setup (width=.5, height=.5)
    window.bgcolor("blue")
    colin = turtle.Turtle()
    colin.shape("turtle")
    colin.color("green")
    colin.width(10)
    colin.speed(10)
    # draw the "c", Colin!
    draw_c(colin)
    macrae = turtle.Turtle()
    macrae.shape("turtle")
    macrae.color("green")
    macrae.speed(10)
    macrae.width(10)
    macrae.up()
    macrae.goto(100,-100)
    macrae.down()
    # draw the "m", MacRae!
    draw_m(macrae)

    window.exitonclick()

draw_initials()
