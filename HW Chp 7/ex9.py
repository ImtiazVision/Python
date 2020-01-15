'''
Imtiaz Ahmed
ex9
Easter Calculation
'''

def main():
    print("Easter Calculator for 1982-2048\n")

    year = int(input("Enter the year: "))
    if 1982 <= year <= 2048:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a + 24) % 30
        e = (2*b + 4*c + 6*d +5)%7

        day = 22 + d + e
        if day > 31:
            print("Easter is on April", day-31)
        else:
            print("Easter is on March", day)
    else:
        print("That's not a year between 1982 and 2048.")

main()
'''
Output:
Easter Calculator for 1982-2048

Enter the year: 2001
Easter is on April 15

Easter Calculator for 1982-2048

Enter the year: 1981
That's not a year between 1982 and 2048.
>>> main()
Easter Calculator for 1982-2048

Enter the year: 1983
Easter is on April 3

'''
