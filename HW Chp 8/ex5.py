'''
Imtiaz Ahmed
Exercise 5
5/12/19
A program that determines if the input value is prime
'''

from math import *
    
def main():
    print("This program determines a prime number\n")
    n = int(input("Enter a value : "))
    if n % 2 == 0:
        print(n, 'is not prime')
        num = 3
        while num <= sqrt(n):
            if n % num == 0:
                print(n, "is not prime")
            num = num + 2
    else:
              
              
        print(n, "is prime.")
    
    
main()

'''
Output:
This program determines a prime number

Enter a value : 5
5 is prime.
>>> main()
This program determines a prime number

Enter a value : 8
8 is not prime


'''
