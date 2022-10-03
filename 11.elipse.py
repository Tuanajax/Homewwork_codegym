import turtle
Tuan_Scr = turtle.Screen()
Tuan_br = turtle.Turtle()
Tuan_Scr.bgcolor('black')
Tuan_br.seth(45)
val=10
ind=0
# turtle speed
turtle.speed(100)
col=['violet','blue','green','yellow',
     'orange','red']
# loop for multiple ellipse
for i in range(36):
    turtle.seth(-val)
    turtle.color(col[ind])
    for i in range(2):
        # turtle.circle(100,90)
        turtle.circle(50,90)
    if ind==5:
        ind=0
    else:
        ind+=1

    val+=10