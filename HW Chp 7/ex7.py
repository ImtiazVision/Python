'''
Imtiaz Ahmed
ex 7
Babysitter 

'''

def main():
    print("Babysitting \n")
    print("Enter times using 24 hour format")
    stHours, stMins = input("Starting time (hh:mm): ").split(":")
    edHours, edMins = input("Ending time (hh:mm): ").split(":")

    
    start = int(stHours) + float(stMins)/60.0
    end = int(edHours) + float(edMins)/60.0

    if end < start: 
        end = end + 24

    bedtime = 22.0
   
    if start < bedtime:
        if end < bedtime:
            primeHours = end - start
            extraHours = 0.0
        else:
            primeHours = bedtime - start
            extraHours = end - bedtime
    else:
        primeHours = 0.0
        extraHours = end - start

    pay = 2.50 * primeHours + 1.75 * extraHours
    print("Total payment due: ${0:0.2f}".format(pay))

main()
'''
Output:
Babysitting 

Enter times using 24 hour format
Starting time (hh:mm): 20:15
Ending time (hh:mm): 23:15
Total payment due: $5.81

Babysitting 

Enter times using 24 hour format
Starting time (hh:mm): 10:25
Ending time (hh:mm): 22:25
Total payment due: $29.69
'''
