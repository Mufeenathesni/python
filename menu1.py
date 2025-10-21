while True:
    print("SELECTION MENU ")
    print("1. Word Count")
    print("2. Letter Frequency")
    print("3. Find Factors")
    print("4. Quit")
    a = int(input("Select an option: "))

    if(a==1):
        text=input("Enter a sentance:")
        words=text.split()
        word_count={}
        for word in words:
            
            if word in word_count:
                
                word_count[word]+=1
            else:
                word_count[word]=+1
            
        for word in word_count:
            print(word,"=",word_count[word])
    

    elif a == 2:
        
        st = input("Enter a word: ")
        if not st.strip():
            print("Empty input detected.")
        else:
            words = st.split()
            for word in words:
                print("\nAnalyzing:",word)
                letter_counts = {}
                for char in word:
                    char_lower = char.lower()
                    letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1
                for char, freq in letter_counts.items():
                    print(char, "appears", freq)

    elif a == 3:
        num=int(input("enter a number"))
        factors=[]
        for i in range(1,num+1):
            if num%i==0:
                factors.append(i)      
        print ("Factors of",num,":",factors)
    elif a == 4:
        print("CLOSING PROGRAM...")
        break

    else:
        print("Invalid option! Choose 1, 2, 3, or 4")
