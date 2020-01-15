# c08ex13.py
#    Graphical Regression Line

from graphics import *

# These two "constants" are defined here so they can be used in multiple
#    functions to draw the done button and check to see if it is clicked in.

DoneX = 1.0   # x coordinate of done button upper right
DoneY = 0.75  # y coordinate of done button upper right

def createWindow():
    # Creates a 500x500 window titled "Linear Regression" and draws
    #    a "Done Button" in the lower left corner. The window coords
    #    run from 0,0 to 10,10, and the upper right corner of the button
    #    is located at (DoneX, DoneY).
    # Returns the window.
    win = GraphWin("Linear Regression", 500, 500)
    win.setCoords(0,0,10,10)
    doneButton = Rectangle(Point(.05,0), Point(DoneX, DoneY))
    doneButton.draw(win)
    Text(doneButton.getCenter(), "Done").draw(win)
    return win

def getPoint(w):
    # w is a GraphWin
    # Pauses for user to click in w. If user clicks somewhere other than
    #    the Done button, the point is drawn in w.
    # Returns the point clicked, or None if user clicked the Done button
    p = w.getMouse()
    if p.getX() > DoneX or p.getY() > DoneY:
        p.draw(w)
        return p
    else:
        return None

def slope(xb, yb, xx, xy, n):
    # Returns the slope of the line of best fit, m
    return (xy - n * xb * yb) / (xx - n*xb*xb)

def predict(x, xb, yb, m):
    # Returns a predicated value for y.
    return yb + m*(x-xb)

def getPoints(w):
    # Allows the user to make a series of mouse clicks in w until
    #    the user clicks in the Done button.
    # Returns: average of x values
    #          average of y values
    #          sum of the squares of the x values
    #          sum of the xy products
    #          the number of points clicked before Done
    sumX = 0.0
    sumY = 0.0
    sumXsq = 0.0
    sumXY = 0.0
    n = 0
    p = getPoint(w)
    while p != None:
        x,y = p.getX(), p.getY()
        sumX = sumX + x
        sumY = sumY + y
        sumXY = sumXY + x * y
        sumXsq = sumXsq + x * x
        n = n + 1
        p = getPoint(w)
    return sumX/n, sumY/n, sumXsq, sumXY, n

def main():
    # Draws a window, gets mouse clicks and then draws line of best
    #   fit through the points that were clicked.
    win = createWindow()
    xbar, ybar, sumXsq, sumXY, n = getPoints(win)
    m = slope(xbar, ybar, sumXsq, sumXY, n)
    y1 = predict(0, xbar, ybar, m)
    y2 = predict(10, xbar, ybar, m)
    regLine = Line(Point(0,y1), Point(10,y2))
    regLine.setWidth(2)
    regLine.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

    
        
