import turtle

t = turtle.Turtle()

turtle.Screen() .bgcolor("black")

t.pensize(2)
t.penup()
#SPEED!!!!#
t.speed(100)

t.penup()
t.goto(-50,-50)
t.color("grey")
t.pendown()

t.goto(100,-50)
t.goto(150,-30)
t.goto(160,30)
t.goto(100,0)
t.goto(0,0)
t.goto(-100,0)
t.goto(-90,15)
t.goto(-100,30)
t.circle(10)

turtle.exitonclick()
