# Imtiaz Ahmed
# 3.25.19
# HW Project
# Ch 3 Ex 2
import math

def main():
    print("This program computes the cost per square inch of a pizza.")
    print()

    diameter = float(input("Enter the diameter of the pizza (in inches): "))
    price = int(input("Enter the price of the pizza (in cents): "))
    area = math.pi * (diameter/2.0)**2
    cost = price /area
    print() 
    print("The cost is", cost, "cents per square inch.")

main()

    
