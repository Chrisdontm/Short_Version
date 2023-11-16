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

t.done()