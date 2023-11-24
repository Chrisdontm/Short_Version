# Short Version
import turtle
import random
import subprocess
s = turtle.getscreen()
s.setup(width=1000, height=1000)
t = turtle

t.penup()
t.goto(0,-400)
t.pendown()
t.speed(1) # This is the slowest that it will draw
		# Speeds go 1 to 10, and then supefast is zero
t.pensize(5)
t.circle(420)
t.pensize(2)
t.speed(0) # This is the fastest that it will draw
t.left(90)
t.forward(380)
t.right(90)
t.circle(40, 22.5)

for i in range(15):  # This is a function that gets repeated 15 times
					# that way you don't have to copy the code 15-times...☺
	t.right(90)
	t.forward(380)
	t.left(180)
	t.forward(380)
	t.right(90)
	t.circle(40, 22.5)

t.right(90)
t.forward(340)
t.left(90)
t.circle(380)


oh1 = 10 # outside circle size of the letter O
noh1 = 4 # straight inside sides of the letter O
cnoh1 = oh1/3 # inside curve inside the O

t.pensize(3)
t.pencolor("red")
t.penup()
t.goto(-23, 27)
t.pendown()
t.circle(cnoh1, 90)
t.forward(noh1)
t.circle(cnoh1, 180)
t.forward(noh1)
t.circle(cnoh1, 90)
t.penup()
t.goto(-23, 22)
t.pensize(3.5)
t.pendown()
t.circle(oh1)
#  Done with O - t.done()

# Onto the letter - N

nh = 20 # height of N
ah = 21 # angle height of N

t.penup()
t.goto(-9, 22)
t.pendown()
t.forward(6)
t.forward(-3)
t.left(90)
t.forward(nh)
t.left(90)
t.forward(3)
t.left(180)
t.forward(6)
t.right(70)
t.forward(ah)
t.left(160)
t.forward(nh)
t.left(90)
t.forward(3)
t.right(180)
t.forward(6)
t.right(180)
t.forward(3)
t.left(90)
t.forward(nh)
t.right(90)
t.forward(3)
t.forward(-6)
t.right(180)
#  Done with N - t.done()

# Onto the letter - E
t.pensize(3.5)
eh = 20 # height of E
#t.pencolor("red")
t.penup()
t.goto(12, 22)
t.pendown()
t.forward(3)
t.left(90)
t.forward(eh)
t.left(90)
t.forward(3)
t.forward(-16)
t.left(90)
t.forward(3)
t.forward(-3)
t.right(90)
t.forward(13)
t.left(90)
t.forward(eh/2)
t.left(90)
t.forward(6)
t.right(90)
t.forward(3)
t.forward(-6)
t.forward(3)
t.right(90)
t.forward(6)
t.left(90)
t.forward(eh/2)
t.left(90)
t.forward(13)
t.left(90)
t.forward(3)
t.left(45)

#  Done with E - t.done()

#  Starting the letter G

oh1 = 10 # outside circle size of the letter G
noh1 = 4 # straight inside sides of the letter G

# t.pensize(3.5)
# t.pencolor("red")
# t.penup()
# t.goto(-15, 14)
# t.pendown()
# t.circle(oh1, 270)
# t.left(45)
# t.forward(noh1)
# t.left(90)
# t.forward(6)
# t.right(180)
#
# #  Done with G - t.done()
#
# oh1 = 10 # outside circle size of the letter O
# noh1 = 4 # straight inside sides of the letter O
# cnoh1 = oh1/3 # inside curve inside the O
#
# t.pensize(3)
# t.pencolor("red")
# t.penup()
# t.goto(0, 2)
# t.pendown()
# t.circle(cnoh1, 90)
# t.forward(noh1)
# t.circle(cnoh1, 180)
# t.forward(noh1)
# t.circle(cnoh1, 90)
# t.penup()
# t.goto(0, -3)
# t.pensize(3.5)
# t.pendown()
# t.circle(oh1)
# #  Done with O - t.done()
#
# oh1 = 10 # outside circle size of the letter D
# noh1 = 6 # straight inside sides of the letter D
#
# t.pensize(3.5)
# t.penup()
# t.goto(14, -3)
# t.pendown()
# t.forward(noh1)
# t.circle(oh1, 180)
# t.forward(noh1)
# t.right(180)
# t.forward(3)
# t.right(90)
# t.forward(20)
# t.left(90)
t.done()