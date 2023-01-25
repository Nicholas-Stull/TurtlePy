import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
turtle.speed(0)
turtle.delay(0)

num_arr = [1272006,555, 777, 333, 222, 111]

for i in range(50000000):
        turtle.forward(random.randint(0,3))
        turtle.color(random.choice(["violet","blue",'red','white','green','yellow']))

        iterator = 0
        if i <= 5:
            turtle.left(num_arr[i])
        #else:
        #    while iterator > 5:
         #       turtle.left(num_arr[iterator])
          #      iterator +=1
        #if iterator == 5:
            #iterator = 0
turtle.exitonclick()
