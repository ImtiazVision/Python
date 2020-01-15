'''
Imtiaz Ahmed
05.15.19
'''
def main():
    print("Exam Grader\n")
    score = int(input("Enter the score: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print("The grade is", grade)

main()
'''
Output:Exam Grader

Enter the score: 45
The grade is F
>>> main()
Exam Grader

Enter the score: 80
The grade is B
>>> 

'''
