# c05ex02.pyw
#    An archery target.

import math
from graphics import *

def targetWindow():
    win = GraphWin("Archery Scorer", 400, 400)
    win.setCoords(-6, -6, 6, 6)
    win.setBackground("gray")
    center = Point(0,0)

    # Draw the target
    c1 = Circle(center, 5)
    c1.setFill("white")
    c1.draw(win)
    c2 = Circle(center, 4)
    c2.setFill("black")
    c2.draw(win)
    c3 = Circle(center, 3)
    c3.setFill("blue")
    c3.draw(win)
    c4 = Circle(center, 2)
    c4.setFill("red")
    c4.draw(win)
    c5 = Circle(center, 1)
    c5.setFill("yellow")
    c5.draw(win)

    return win


def drawInterface(win):
    msg = Text(Point(0,5.5), "Click where arrow lands")
    msg.setStyle("bold")
    msg.setSize(14)
    msg.draw(win)

    arrowBox = Text(Point(-4,-5.5),"Arrow:  ")
    arrowBox.setStyle("bold")
    arrowBox.draw(win)

    totalBox = Text(Point(4,-5.5), "Total:   ")
    totalBox.setStyle("bold")
    totalBox.draw(win)

    return msg, arrowBox, totalBox


def getScore(pt):
    x,y = pt.getX(), pt.getY()
    dist = math.sqrt(x*x + y*y)
    if dist <= 1:
        score = 9
    elif dist <= 2:
        score = 7
    elif dist <=3:
        score = 5
    elif dist <= 4:
        score = 3
    elif dist <= 5:
        score = 1
    else:
        score = 0
    return score

        
def main():
    win = targetWindow()
    msg, arrowBox, totalBox = drawInterface(win)

    arrow = 0
    total = 0
    for i in range(5):
        hit = win.getMouse()
        dot = Circle(hit, 0.1)
        dot.setFill("green")
        dot.draw(win)
        score = getScore(hit)
        arrowBox.setText("Arrow: {0:1}".format(score))
        total = total + score
        totalBox.setText("Total: {0:2}".format(total))

    msg.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()
