def main():

    print("This program turns a lowercase word into an Uppercase one")

    word = input("Enter the lowercase word:  " )

    print("The lowercase word is: ")

    for ch in word:
        ch = (ord(ch) - 32)
        print(chr(ord), end= "")
main()
          
        
