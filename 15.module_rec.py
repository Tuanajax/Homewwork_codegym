import turtle
Tuan_Scr = turtle.Screen()
Tuan_br = turtle.Turtle()
def rec(l,w):
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

Tuan_br.penup()
Tuan_br.goto(100,100)
rec(100,300)
Tuan_br.penup()
Tuan_br.goto(0,100)
Tuan_br.left(90)
rec(100,300)