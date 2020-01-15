# Imtiaz Ahmed
# 3.25.19
# HW Project
# Chapter 4 Example 7
from graphics import *
import math

def main():
    print("This program computes circle intersection with a horizontal line")
   
    print()

    radius = float(input("Please enter the radius : "))
    yintercept = float(input("Please enter the y-intercept: "))

    win = GraphWin("Circle Intersection")
    win.setCoords(-10,-10,10,10)

    Circle(Point(0,0), radius).draw(win)
    Line(Point(-10,yintercept), Point(10,yintercept)).draw(win)

    x = math.sqrt(radius * radius - yintercept * yintercept)
    print("X values of intersection", -x, x)

    p1 = Circle(Point(x,yintercept),0.25)
    p1.setOutline("red")
    p1.setFill("red")
    p1.draw(win)

    p2 = p1.clone()
    p2.move(-2*x, 0)
    p2.draw(win)

    win.getMouse()
    win.close()

main()
