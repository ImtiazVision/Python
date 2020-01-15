'''
Imtiaz Ahmed
Exercise 2
5/12/19
Windchill Table
'''

def windChill(T, V):
    if V > 3:
        formula = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
    else:
        formula = T
    return formula

def main():

    print("Wind Chill Index ")
    print("                         Temperature")
    print("MPH ", end=' ')
    temperature = list(range(-20,61,10))
    for T in temperature:
        print("{0:5}".format(T), end=' ')
    print("\n__________________________________________________________")


    for spd in range(0,51,5):
        print("{0:4}".format(spd), end= ' ')
        for temps in temperature:
            print("{0:5.0f}".format(windChill(temps, spd)), end=' ')
        print()
    print()

main()

'''
Output:
Wind Chill Index 
                         Temperature
MPH    -20   -10     0    10    20    30    40    50    60 
__________________________________________________________
   0   -20   -10     0    10    20    30    40    50    60 
   5   -34   -22   -11     1    13    25    36    48    60 
  10   -41   -28   -16    -4     9    21    34    46    58 
  15   -45   -32   -19    -7     6    19    32    45    57 
  20   -48   -35   -22    -9     4    17    30    44    57 
  25   -51   -37   -24   -11     3    16    29    43    56 
  30   -53   -39   -26   -12     1    15    28    42    56 
  35   -55   -41   -27   -14     0    14    28    41    55 
  40   -57   -43   -29   -15    -1    13    27    41    55 
  45   -58   -44   -30   -16    -2    12    26    40    54 
  50   -60   -45   -31   -17    -3    12    26    40    54 

'''
