list1 = list(map(int, input("Enter list 1 numbers separated by space: ").split()))
list2 = list(map(int, input("Enter list 2 numbers separated by space: ").split()))
length=len(list1) == len(list2)
if(length):
    print("Two strings are  same length:",length)
else:
    print("Two strings are no same length:",length)
add=sum(list1) == sum(list2)
if(add):
    print("Same sum:",add)
else:
    print("Different sum",add)
common = set(list1) & set(list2)
if(common):
    print("Common values:",common)
else:
    Print("none")
