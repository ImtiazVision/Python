# Imtiaz Ahmed
# 3.25.19
# HW Project
# Ch3ex13
def main():
    print("This program sum up some numbers")
    print()

    n = int(input("Numbers to be summed: "))
    total = 0
    for i in range(n):
        num = float(input("Enter a number: "))
        total +=  num

    print()
    print("The sum of the numbers is:", total)

main()
