text=str(input("Enter the words:"))
count_a=0
for name in text:
    count_a += name.lower().count('a')
print("Total occurance of a:",count_a)
