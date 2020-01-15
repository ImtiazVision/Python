'''
Imtiaz Ahmed
5.12.19
Exercise 7
Goldbach conjecture
'''


from math import *
    
def main1(n):
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
    
    


def goldbach(x):
    num1 = 3
    while num1 < x/2:
        num2 = x - num1
        if main1(num1) and  main1(num2):
            return num1
        num1 = num1 + 2

def main():
    print("Goldbach Conjecture\n")
    
    n = int(input("Enter an even natural number: "))
    if n % 2 != 0:
        print(n, "is not even!")
    else:
        prime1 = goldbach(n)
        prime2 = n - prime1
        print("{0} + {1} = {2}".format(prime1, prime2, n))
main1(8)
main()
