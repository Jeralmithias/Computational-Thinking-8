# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 = 150
x2 = -200
y2 = 50
x3 = -200
y3 = -50
x4 = -200
y4 = -150

# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("cornfield")
t1 = create_sprite("kitten",x1,y1)
t2 = create_sprite("soccerball",x2,y2)
t3 = create_sprite("fox",x3,y3)
t4 = create_sprite("fish",x4,y4)
time.sleep(1.0)


# # Section 4 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
# sprite 1 is the fastest sprite in theory because it has the highest low value of all the sprites
# sprite 3 and 4 are the slowest because in theory they would on avrage go less distance than the other 2 becouse of their higher points unless sprite 2 gets un lucky and roles a -1 
for i in range(30):
    x1 += random.randint(5,15)
    x2 += random.randint(-1,18)
    x3 += random.randint(0,15)
    x4 += random.randint(0,15)
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    time.sleep(0.1)


# # Section 5 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
	print("player 2 wins!")
if x3 >= x1 and x3 >= x2 and x3 >= x4:
	print("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
	print("player 4 wins!")
if x1 == x2 and x2 == x3 and x4 == x1:
	print("Tie!")
 





turtle.exitonclick()


