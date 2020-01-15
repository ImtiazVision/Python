# Imtiaz Ahmed
# 3.25.19
# HW Project
# Ch3ex12
def main():
    print("This program finds the sum of the cubes of the first n natural numbers.")
    print()

    n = int(input("Please enter a value for n: "))
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**3

    print()
    print("The sum of cubes of 1 through", n, "is:", sum)

main()
