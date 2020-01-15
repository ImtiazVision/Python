# Imtiaz Ahmed
# 3.25.19
# HW Project
# Chapter 4 example 1
from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(40,40), Point(60,60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape = shape.clone()
        shape.move(dx,dy)
        shape.draw(win)
    Text(Point(113,175), "Click again to quit.").draw(win)
    win.getMouse()
    win.close()

main()
