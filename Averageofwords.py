def main():

    Sentence= input("Enter sentence")
    words = Sentence.split(" ")
    Sum = 0 # addictive identity

    for i in words:
        Sum = Sum + len(i)
        average = Sum/len(words)
    print(average)

main()

    
