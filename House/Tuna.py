from math import cos, radians
import turtle
Tuan_Scr = turtle.Screen()
Tuan_br = turtle.Turtle()
def rec(l,w):
    ''' draw rectangle
    l(float): length
    w(float): width'''
    Tuan_br.pendown()
    Tuan_br.fillcolor("red")
    Tuan_br.begin_fill()
    Tuan_br.fd(l)
    Tuan_br.left(90)
    Tuan_br.fd(w)
    Tuan_br.left(90)
    Tuan_br.fd(l)
    Tuan_br.left(90)
    Tuan_br.fd(w)
    Tuan_br.end_fill()
    Tuan_br.penup()

def tri(b,a):
    ''' Draw triangle
    b(int): base
    a(degree): angle'''
    Tuan_br.pendown()
    Tuan_br.fd(b)
    h = 0.5*b/cos(radians(a))
    Tuan_br.left(180-a)
    Tuan_br.fd(h) 
    Tuan_br.left(2*a)
    Tuan_br.fd(h) 