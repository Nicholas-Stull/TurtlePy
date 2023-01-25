import turtle
import random

wn = turtle.Screen()
wn.bgcolor('black')
turtle.speed(1000)

colors = ['blue','red']

for i in range(15000):
	if i%2 == 0:
		turtle.forward(2*i)
		turtle.right(666)
		turtle.color(colors[0])
	else:
		turtle.forward(2*i)
		turtle.right(666)
		turtle.color(colors[1])
turtle.exitonclick()
