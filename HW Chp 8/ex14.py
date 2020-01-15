# c08ex14.py
#  Convert image to grayscale

from graphics import *

def openImage(picFile):
    img = Image(Point(0,0), picFile)
    width = img.getWidth()
    height = img.getHeight()
    img.move(width//2, height//2)
    win = GraphWin(picFile, width, height)
    img.draw(win)
    return img

def convertToGray(img):
    for row in range(img.getWidth()):
        for col in range(img.getHeight()):
            r, g, b = img.getPixel(row,col)
            i = round(0.299*r + 0.587*g + 0.114*b)
            img.setPixel(row,col, color_rgb(i,i,i))
        update()


def main():
    print("This program converts an image to grayscale.")

    inFile = input("Enter the name of a GIF file to convert: ")
    image = openImage(inFile)

    print("Converting...", end="")
    convertToGray(image)
    print("Done.")
    
    outFile = input("Enter filename for the converted image: ")
    image.save(outFile)

main()
