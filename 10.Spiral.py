from os import curdir
from re import A
import turtle
Tuan_Scr = turtle.Screen()
Tuan_br = turtle.Turtle()
Home_=turtle.home()
d = 1
while True:
    Tuan_br.fd(d)
    Tuan_br.left(15)
    A = Tuan_br.pos()
    d+=3
    if Tuan_br.distance(A) == 100:
        break
print(A)
    