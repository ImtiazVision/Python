'''
Imtiaz Ahmed
Exercise 3
5/12/19
How long is it take for an Investment to double at a given interest rate using
While loop
'''
def main():
    print("Number of years for an investment to double.\n")

    apr = float(input("What is the annual interest rate? "))
    principal = 1
    years = 0
    while principal < 2:
        principal = principal*(1+apr)
        years = years + 1

    print("Years would take for the investment to double:", years)

    

main()
'''
Output:
Number of years for an investment to double.

What is the annual interest rate? 6
Years would take for the investment to double: 1
>>> main()
Number of years for an investment to double.

What is the annual interest rate? 1
Years would take for the investment to double: 1

>>> main()
Number of years for an investment to double.

What is the annual interest rate? 0.2
Years would take for the investment to double: 4
>>> 
'''
