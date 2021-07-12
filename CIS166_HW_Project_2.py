'''
Imtiaz Ahmed
HW Project 2
4.28.19
'''
from graphics import *
def main():
    win = GraphWin("Weight Converter", 500,500)
    win.setCoords(0.0,0.0,8.0,8.0)
    label = Text(Point(4,7.5), "Weight Converter")
    label.setSize(14)
    label.setStyle('bold')
    label.draw(win)
    rectangle = Entry(Point(4,7), 25)
    rectangle.setText("0.0")
    rectangle.setFill('white')
    rectangle.draw(win)
    label1 = Text(Point(6,7), "lb")
    label1.draw(win)

    rectangle4 = Rectangle(Point(6.5,.8), Point(7.5,1.2)).draw(win)
    rectangle4.setFill('orange')

    button = Text(Point(7, 1.0), "Convert")
    button.setTextColor('white')
    button.draw(win)

    
    
    label2= Text(Point(2.7,6.5),"Grams")
    label2.draw(win)
    rectangle1 = Entry(Point(4,6), 25)
    rectangle1.setFill('white')
    rectangle1.setText("0.0")
    rectangle1.draw(win)
    win.getMouse()
    
    label3 = Text(Point(2.7,5.5), "  Kilograms")
    label3.draw(win)
    rectangle2 = Entry(Point(4,5),25)
    rectangle2.setFill('white')
    rectangle2.setText("0.0")
    rectangle2.draw(win)
    
    
    label4 = Text(Point(2.7, 4.5), "Ounce")
    label4.draw(win)
    rectangle3 = Entry(Point(4,4), 25)
    rectangle3.setFill('white')
    rectangle3.setText("0.0")
    rectangle3.draw(win)
    
    
    
    
    lb = eval(rectangle.getText())
    grams = lb*453.59
    rectangle1.setText(grams)
    win.getMouse()

    lb1 = eval(rectangle1.getText())
    kg = lb1/1000
    rectangle2.setText(kg)
    win.getMouse()

    lb2 = eval(rectangle2.getText())
    oz = lb2*35.274
    rectangle3.setText(oz)
    win.getMouse()
   

   
    win.close()

    
main()


