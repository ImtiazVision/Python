from graphics import *
import math

def main():

    win = GraphWin("Triangle:)",500,500)

    win.setCoords(0,0,10,10)
    message = Text(Point(5,1),"Click On Three points")
    message.draw(win)
    
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    tri = Polygon(p1,p2,p3)
    tri.setFill("peachpuff")
    tri.setOutline("cyan")
    tri.draw(win)

   
    
    win.getMouse()
    win.close()

main()
