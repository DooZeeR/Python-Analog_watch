import time
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analóg Óra")
wn.tracer(0)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def ora(pen):

    pen.penup()
    pen.goto(0, 200)
    pen.setheading(180)
    pen.color("#106200")
    pen.pensize(2)
#    pen.pendown()
    pen.circle(200)
    pen.color("White")
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    
    for i in range(60):
        if i==0:
            pen.forward(175)
            pen.pensize(4)
            pen.color("#20ec00")
            pen.pendown()
            pen.forward(15)
            pen.penup()
            pen.goto(0,0)
            pen.rt(6)
            pen.color("white")
        elif i > 0 and i % 5 == 0:
            pen.forward(175)
            pen.pensize(4)
            pen.color("#25ec00")
            pen.pendown()
            pen.forward(15)
            pen.penup()
            pen.goto(0,0)
            pen.rt(6)
            pen.color("white")
        else:
            pen.forward(185)
            pen.pensize(1)
            pen.color("#1cb100")
            pen.pendown()
            pen.forward(5)
            pen.penup()
            pen.goto(0,0)
            pen.rt(6)
            pen.color("white")
        
def orah(h,m,pen):
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    szog = ((h / 12) * 360)+(m/2)
    pen.rt(szog)
    pen.pensize(7)
    pen.color("#9cff8a")
    pen.pendown()
    pen.forward(95)
    pen.color("white")
    
def oram(m,s,pen):
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    szog = ((m / 60) * 360)+(s*0.1)
    pen.rt(szog)
    pen.pensize(3)
    pen.color("#9cff8a")
    pen.pendown()
    pen.forward(140)
    pen.color("white")

def oras(s,pen):
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    szog = (s / 60) * 360
    pen.rt(szog)
    pen.pensize(1)
    pen.color("#ff2000")
    pen.pendown()
    pen.forward(170)
    pen.color("White")

def szam(pen):
    pen.penup()
    pen.goto(-9,-15)
    pen.setheading(90)
    for i in range(1, 13):
        pen.penup()
        pen.goto(-10,-15)
        pen.rt(30)
        pen.pensize(2)
#        pen.color("#25ec00")
        pen.color("#9cff8a")
        pen.forward(155)
        pen.pendown()
        pen.write(i,  font=("Arial", 18, "normal"))
        pen.penup()
    
    
while 1:
    ido = (time.localtime())
    h = ido[3]
    m = ido[4]
    s = ido[5]
    ora(pen)
    szam(pen)
    orah(h,m, pen)
    oram(m,s, pen)
    oras(s, pen)
    wn.update()
    time.sleep(1)
    pen.clear()
wn.mainloop()
