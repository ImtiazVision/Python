'''
Imtiaz Ahmed
ex 10
Easter from 1900 - 2099
'''
def main():
    print("Easter Calculator for 1900-2099\n")

    year = int(input("Enter the year: "))
    if 1900 <= year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a + 24) % 30
        e = (2*b + 4*c + 6*d +5)%7

        day = 22 + d + e

        
        if year in [1954, 1981, 2049, 2076]:
            day = day - 7
            
        if day > 31:
            print("Easter is on April", day-31)
        else:
            print("Easter is on March", day)
    else:
        print("That's not a year between 1900 and 2099.")

main()

'''
Output:
Easter Calculator for 1900-2099

Enter the year: 1991
Easter is on March 31

Easter Calculator for 1900-2099

Enter the year: 2088
Easter is on April 11
>>> main()
Easter Calculator for 1900-2099

Enter the year: 2099
Easter is on April 12
>>> main()
Easter Calculator for 1900-2099

Enter the year: 2096
Easter is on April 15
>>> main()
Easter Calculator for 1900-2099

Enter the year: 2092
Easter is on March 30
>>> 
'''
