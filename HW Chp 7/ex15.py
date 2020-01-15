'''
Imtiaz Ahmed
ex 15
'''
import math

from graphics import *

def main():
    win = GraphWin("Line Segment Info", 400, 400)
    win.setCoords(-10,-10,10,10)

    msg = Text(Point(0,-9.5), "Click on endpoints of a line segment.")
    msg.draw(win)

    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    line = Line(p1,p2)
    line.draw(win)

    mark = Circle(line.getCenter(),0.15)
    mark.setFill("cyan")
    mark.draw(win)

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    if dx != 0.0:
        slope = str(round(dy/dx,2))
    else:
        slope = "inf"
    length = str(round(math.sqrt(dx*dx + dy*dy),2))

    msg.setText("Length: {}, Slope: {}".format(length, slope))
    win.getMouse()
    win.close()

main()
              
