'''
Imtiaz Ahmed
Exercise 4
5/12/19
 Syracuse sequence
'''

def main():
    print("This program outputs a Syracuse sequence")
    
    n = int(input("Enter the initial value that is greater than 1 : "))
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    print(1)

main()
'''
Output:

This program outputs a Syracuse sequence
Enter the initial value that is greater than 1 : 3
3 10 5.0 16.0 8.0 4.0 2.0 1
>>> main()
This program outputs a Syracuse sequence
Enter the initial value that is greater than 1 : 5
5 16 8.0 4.0 2.0 1
'''
