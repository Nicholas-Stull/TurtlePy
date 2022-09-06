import turtle
import random

wn = turtle.Screen()
wn.bgcolor('black')
turtle.speed(1000)

colors = ['blue','red']

for i in range(800):
	if i%2 == 0:
		turtle.forward(2*i)
		turtle.right(3.1415926535897*10)
		turtle.color(colors[0])
	else:
		turtle.forward(2*i)
		turtle.right(2.7182818284590*10)
		turtle.color(colors[1])
turtle.exitonclick()
