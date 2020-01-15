# Imtiaz Ahmed
# 3.25.19
# HW Project
# Ch 2 Ex1
import math

def main():
    print("This program computes the volume and surface area of a sphere")
    print()

    radius = float(input("Please enter the radius of the sphere: "))
    volume = 4.0/3.0 * math.pi * radius**3
    area = 4 * math.pi * radius**2

    print("The volume is", volume, "cubic units.")
    print("The surface area is", area, "square units.")

main()
