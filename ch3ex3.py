# Imtiaz Ahmed
# 3.25.19
# HW Project
# Chapter 3 Ex 3
def main():
    print("This program calculates the molecular weight of a hydrocarbon.")
    print()

    hyd = int(input("Enter the number of hydrogen atoms: "))
    car = int(input("Enter the number of carbon atoms: "))
    oxy = int(input("Enter the number of oxygen atoms: "))
    molecular_weight = 1.00794 * hyd + 12.0107 * car + 15.9994 * oxy

    print()
    print("The molecular weight is:", molecular_weight)

main()
