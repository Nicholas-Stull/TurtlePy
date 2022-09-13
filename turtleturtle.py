import random
from tkinter import *
from turtle import *
import turtle

wn = turtle.Screen()
wn.bgcolor('black')
turtle.speed(0)

colors = ['#C4E0F8','#F4A2E9']
rand = random.randint(100,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999*10*10)


for i in range(10):
    turtle.forward(5*i)

    #Replace with number in photo.
    turtle.right(rand)
    print(i)
	
    if i%2 == 0:
        turtle.color(colors[0])
    else:
        turtle.color(colors[1])







