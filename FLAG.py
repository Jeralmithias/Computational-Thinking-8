import turtle
t = turtle.Turtle()

height = 50
# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")


# stripes
t.penup()
# move to stripe 1
t.goto(-250, -100)
t.pendown()
# stripe 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -50)

# stripe 2
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 3
t.goto(-250, 0)

# stripe 3
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 4
t.goto(-250, 50)

# stripe 4
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 5
t.goto(-250, 100)

# stripe 5
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


# blue square
t.goto(-250, 50)
t.color("blue")
t.begin_fill()
t.forward(130)
t.left(90)
t.forward(100)
t.left(90)
t.forward(130)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.penup()
# stars
t.color("white")
t.goto(-245,100)
t.pendown()
t.begin_fill()
for i in range(5):
        t.forward(75)
        t.right(144)
t.end_fill()
t.penup()
t.goto(-250, 1000)
turtle.exitonclick()
