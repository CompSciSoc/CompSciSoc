import turtle
import tilt

while True:
    mgx, mgy = tilt.getTiltData()
    print(mgx, mgy)
    pos = turtle.pos()
    turtle.goto(pos[0] + round(mgx), pos[1] - round(mgy))