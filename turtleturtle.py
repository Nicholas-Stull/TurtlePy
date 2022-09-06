import turtle
import random
wn = turtle.Screen()
wn.bgcolor('black')
turtle.speed(1000)

colors = ['blue','red']

for i in range(800):
    turtle.forward(5*i)

    #Replace with number in photo.
    turtle.right(3.141)

    if i%2 == 0:
        turtle.color(colors[0])
    else:
        turtle.color(colors[1])

turtle.exitonclick()
