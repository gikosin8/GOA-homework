from turtle import *


#we want to paint a house

#step 1: draw a squar
width(7)
color("red")
forward(200)
left(90)

forward(200)
left (90)

forward(200)
left (90)

forward(200)
left (90)


#and of square

#drawing a door

forward(70)     #height of the door
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto (200, 200)
pendown()

color("red")
begin_fill() 
right(150)
forward(200)
left(120)
forward(200)
end_fill()


exitonclick()