# c08ex14.py
#  Convert image to color negative

from graphics import *

def openImage(picFile):
    img = Image(Point(0,0), picFile)
    width = img.getWidth()
    height = img.getHeight()
    img.move(width//2, height//2)
    win = GraphWin(picFile, width, height)
    img.draw(win)
    return img

def convertToNegative(img):
    for row in range(img.getWidth()):
        for col in range(img.getHeight()):
            r, g, b = img.getPixel(row,col)
            img.setPixel(row,col, color_rgb(255-r,255-g,255-b))
        update()


def main():
    print("This program converts an image to a negative.")

    inFile = input("Enter the name of a GIF file to convert: ")
    image = openImage(inFile)

    print("Converting...", end="")
    convertToNegative(image)
    print("Done.")
    
    outFile = input("Enter filename for the converted image: ")
    image.save(outFile)

main()
