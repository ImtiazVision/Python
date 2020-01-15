'''
Imtiaz Ahmed
ex 5
Body mass index
'''

def main():
    print("Body Mass Index Calclator\n")

    weight = int(input("Enter your weight (in pounds): "))
    height = int(input("Enter you height (in inches): "))
    bmi = (720 * weight) / height**2

    print("Your BMI is", bmi)
    if bmi < 19:
        print("It below healthy range.")
    elif bmi <= 25:
        print("That's in the healthy range.")
    else:
        print("That's aboove healthy range.")

main()


'''
Output:
Body Mass Index Calclator

Enter your weight (in pounds): 90
Enter you height (in inches): 65
Your BMI is 15.337278106508876
It below healthy range.
>>> main()
Body Mass Index Calclator

Enter your weight (in pounds): 160
Enter you height (in inches): 65
Your BMI is 27.266272189349113
That's aboove healthy range.

'''
