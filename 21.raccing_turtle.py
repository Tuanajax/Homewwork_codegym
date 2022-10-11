from datetime import datetime
from doctest import script_from_examples
from operator import truediv
from tracemalloc import start
import turtle as t
import random

# Make road:
Scr = t.Screen()
Scr.setup(height=500,width=600)
pen = t.Turtle(visible=False)
pen.penup()
pen.speed(0)
pen.goto(-250,200)
for i in range(21):
    pen.write(i)
    pen.forward(25)

# Draw dash-lines
x =-250
pen.goto(-250,200)
pen.right(90)
for i in range(21):
    for j in range(10):
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.fd(10)
    pen.penup()
    pen.fd(5)
    pen.write(i)
    pen.goto(x+(i+1)*25,200)

# Make turtles:
all_turtles=[]
y_pos = [160,100,40,-20]
colors = ['red','green','blue','purple']
for i in range(0,4):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    turtles.goto(x=-250,y=y_pos[i])
    turtles.color(colors[i])
    for i in range(5):
        turtles.left(72)
    all_turtles.append(turtles)

def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 250:
            b = colors[all_turtles.index(turtle)]
            print(f"The {b} turtle win! ")
            run = False
# start_ = input("Start(y/n): ")
# if start_.upper =="y": run = True
# else: run = False
run = True
start = datetime.now()
while run:
    for i in range(4): 
        random_walk(all_turtles)
print(" With time: ", datetime.now()-start)
Scr.exitonclick()
    