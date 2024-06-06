import turtle
import tilt

while True:
    mgx, mgy = tilt.getTiltData()
    pos1 = turtle.pos()
    turtle.goto(pos1[0] + mgx/100, pos1[1] - mgy/100)