# Imtiaz Ahmed
# 3.25.19
# HW Project
# Chapter 3 example 16
def main():
    print("This program computes the nth Fibonacci number.")
    print()

    n = int(input("Enter the value of n: "))
    current, previous = 1, 1
    for i in range(n-2):
        current, previous = current + previous, current

    print()
    print("The nth Fibonacci number is", current)

main()
