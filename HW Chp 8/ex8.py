'''
Imtiaz Ahmed
Exercise 1 Review
5/19/19
Euclid's algorithm for GCD
'''

def gcd(m,n):
    while m != 0:
        n, m = m, n % m
    return n

def main():
    print("Euclid's GCD algorithm\n")
    x1, x2 = input("Enter two natural numbers (n1, n2): ").split(",")
    
    print("The GCD of", x1, "and", x2, "is", gcd(int(x1),int(x2)))

main()

'''
Output:
Euclid's GCD algorithm

Enter two natural numbers (n1, n2): 4,9
The GCD of 4 and 9 is 1

Euclid's GCD algorithm

Enter two natural numbers (n1, n2): 5,25
The GCD of 5 and 25 is 5
'''
