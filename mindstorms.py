import turtle

def draw_square():
    window = turtle.Screen()
    window.setup (width=.5, height=.5)
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black", "green")
    brad.speed(1)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.bye()


draw_square()
