'''
Imtiaz Ahmed
Exercise 5
5/12/19
Program to figure out gas mileage overa multiple-leg journey.
'''
def main():
    print("This program calculates fuel efficiency over a multi-leg journey.")
    print("\n")
    print("Click Enter to finish\n")
    print("\n")
          

    distance, fuel = 0.0, 0.0
    inStr = input("Enter gallons and miles with coma in da middle: ")
    while inStr != "":
        inputs = inStr.split(",")
        gallons, miles = int(inputs[0]), int(inputs[1])
        print("MPG for this leg: {0:0.1f}".format(miles/gallons))
        distance = distance + miles
        fuel = fuel + gallons
        inStr = input("Enter gallons and miles with coma in da middle: ")

    print()
    print("You have traveled a total of {0:0.1f} miles on {1:0.1f} gallons."
          .format(distance, fuel))
    print("The fuel efficiency was {0:0.1f} miles per gallon."
          .format(distance/fuel))

main()

'''
Output:

This program calculates fuel efficiency over a multi-leg journey.


Click Enter to finish



Enter gallons and miles with coma in da middle: 45,2
MPG for this leg: 0.0
Enter gallons and miles with coma in da middle: 45,28
MPG for this leg: 0.6
Enter gallons and miles with coma in da middle: 3,25
MPG for this leg: 8.3
Enter gallons and miles with coma in da middle: 

You have traveled a total of 55.0 miles on 93.0 gallons.
The fuel efficiency was 0.6 miles per gallon.


'''
