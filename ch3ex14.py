# Imtiaz Ahmed
# 3.25.19
# HW Project
# Chapter 3 example 14
def main():
    print("This program  calculates average")
    print()

    n = int(input("How many numbers we have? "))
    total = 0
    for i in range(n):
        num = float(input("Enter a number: "))
        total = total + num # total += num

    print()
    print("The average of the numbers is:", total/n)

main()
