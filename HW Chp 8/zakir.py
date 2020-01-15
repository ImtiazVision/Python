def zakir():
   first = 1
   second = 1
   count = 2
   currentnumber = 0    
   userinput = int(input('Enter a number'))
   if (userinput == 1 or userinput == 2):
        print (1)
   while(count < userinput):        
        currentnumber = first + second
        first  = second
        second = currentnumber
        count = count + 1
        print('Currently we are counting ' + str(count) + 'number')
        print (count)
        print(currentnumber)        
   print('final answer')
   print(currentnumber)
   
readytoplay = int(input('Ready? 1 for yes, 0 for no.  Please enter'))
while(readytoplay == 1):
    zakir()
    readytoplay = int(input('Ready? 1 for yes, 0 for no.  Please enter'))
    



        
        
