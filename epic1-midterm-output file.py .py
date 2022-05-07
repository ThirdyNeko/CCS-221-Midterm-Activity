#Ireneo Catequista III

#Initializing
import turtle
from turtle import *

#colors
bgcolor('black')
col=['violet','blue','green','yellow','orange','red']
i = 0

#speed
speed(1000)

#shapes
def draw_eclipse(r):
    for i in range(2):
            circle(r,90)
            circle(r//2,90)

# eclipses
x = 36
val = 10
while x != 0:
    seth(-val)
    color(col[i])
    if i == 5:
        i = 0
    else:
        i += 1
    begin_fill()
    draw_eclipse(80)
    end_fill()

    val+=10
    x -= 1


#inner circles
x = 50
left(90)
penup()
forward(50)
pendown()
left(90)
while x != 0:
    begin_fill()
    color(col[i])
    if i == 5:
        i = 0
    else:
        i += 1
    circle(x)
    left(90)
    penup()
    forward(10)
    pendown()
    right(90)
    x -= 10
    end_fill()

#outer eclipses
x = 4
val = 10
if i == 5:
    i = 0
else:
    i += 1
while x != 0:
    seth(-val)
    
    color(col[i])
    draw_eclipse(100)
    x -= 1
    val+=90

#outer circles
if i == 5:
    i = 0
else:
    i += 1
color(col[i])
x = 10
y = 165
right(90)
penup()
forward(165)
pendown()
left(90)
while x != 0:
    circle(y)
    left(90)
    penup()
    forward(5)
    pendown()
    right(90)
    y -= 5
    x -= 1

done()