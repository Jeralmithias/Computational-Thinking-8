import turtle

t = turtle.Turtle()

turtle.Screen() .bgcolor("black")

t.pensize(2)
t.penup()
#SPEED!!!!#
t.speed(100)

#The code for the big red circle
t.penup()
colors = ["white","light green","red"]
t.goto(-38, -45)
t.pendown()
for i in range(110) :
    t.pendown()
    t.color( colors [ i % 3 ] )
    t.forward(58)
    t.left(28)
    t.forward( 9 + i )
    t.left( 28 + 1)
###############################
    t.penup()
colors = ["purple","pink","white"]
t.goto(-200, -100)
t.pendown()
for i in range(110) :
    t.pendown()
    t.color( colors [ i % 3 ] )
    t.forward(30)
    t.left(85)
    t.forward( 9 + i )
    t.left( 28 + 1)

t.penup()
colors = ["red","yellow","orange"]
t.goto(-10, -50)
t.pendown()
for i in range(100) :
    t.pendown()
    t.color( colors [ i % 3 ] )
    t.forward(27)
    t.left(120)
    t.forward( 10 + i )
    t.left( 30 + 1)


    t.penup()
colors = ["blue","red","white"]
t.goto(200,200)
t.pendown()
for i in range(100) :
    t.pendown()
    t.color( colors [ i % 3 ] )
    t.forward(33)
    t.left(78)
    t.forward( 8 + i )
    t.left( 48 + 1)

# The last colored circle #
t.penup()
# Makes it turn colors #
colors = ["blue","purple","white"]
t.goto(200, -100)
t.pendown()
for i in range(100) :
    t.pendown()
    t.color( colors [ i % 3 ] )
    t.forward(33)
    t.left(78)
    t.forward( 8 + i )
    t.left( 48 + 1)
#######################################


turtle.exitonclick()