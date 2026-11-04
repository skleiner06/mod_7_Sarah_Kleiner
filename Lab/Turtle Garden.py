import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("purple")
pen.speed(3)

pen.fillcolor("yellow")

pen.begin_fill()

for side in range(4):
    pen.forward(100)
    pen.left(90)

pen.end_fill()

screen.exitonclick()