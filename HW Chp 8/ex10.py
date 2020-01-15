# c08ex10.py
#     Batch fuel efficiency

def main():
    print("This program calculates fuel efficiency over a multi-leg journey.")
    print("It gets trip information from a file. Each line of the file should")
    print("have the gallons used and miles traveled (separated by a comma) for")
    print("one leg of the journey.\n")

    fname = input("What file contains the data? ")
    infile = open(fname,'r')

    distance, fuel = 0.0, 0.0
    for line in infile:
        inputs = line.split(",")
        gallons, miles = int(inputs[0]), int(inputs[1])

        print("Gallons: {0:0.1f}, Miles: {1:0.1f}, MPG: {2:0.1f}"
              .format(gallons, miles, miles/gallons))
        distance = distance + miles
        fuel = fuel + gallons
    infile.close()
    
    print("\nYou traveled a total of {0:0.1f} miles on {1:0.1f} gallons."
          .format(distance, fuel))
    print("The fuel efficiency was {0:0.1f} miles per gallon."
          .format(distance/fuel))

if __name__ == '__main__':
    main()
