a=int(input("Enter a 1st number:"))
b=int(input("Enter a 2nd number:"))
c=int(input("Enter a 3rd number:"))
if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print("The greatest number is:", greatest)
