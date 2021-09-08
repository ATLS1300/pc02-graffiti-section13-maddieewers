#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: MADDIE EWERS
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()
turtle.goto(25,115)
turtle.pensize(5)
turtle.begin_fill()
turtle.color("chartreuse2")
turtle.down()
turtle.forward(30)
turtle.left(90)
turtle.forward(17)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(17)
turtle.end_fill()
turtle.up()
turtle.goto(35,120)
turtle.down()
turtle.right(90)
turtle.forward(30)
turtle.up()
turtle.color("chartreuse2")
turtle.begin_fill()
turtle.left(90)
turtle.down()
turtle.forward(15)
turtle.right(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(3)
turtle.end_fill()
turtle.up()
turtle.goto(70,-90)
turtle.pensize(10)
turtle.left(90)
turtle.left(60)
turtle.color("azure")
turtle.down()
turtle.forward(100)
turtle.up()
turtle.color("DeepPink1")
turtle.begin_fill()
turtle.right(60)
turtle.forward(30)
turtle.down()
turtle.circle(50)
turtle.end_fill()
turtle.color("DarkOrange")
turtle.up()
turtle.forward(200)
turtle.down()
turtle.left(120)
turtle.forward(250)
turtle.left(45)
turtle.forward(250)
turtle.left(45)
turtle.forward(250)
turtle.left(45)
turtle.forward(250)
turtle.left(45)
turtle.forward(250)
turtle.left(45)
turtle.forward(250)
turtle.left(45)
turtle.forward(250)
turtle.left(45)
turtle.forward(250)
turtle.up()
turtle.bye()












#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
