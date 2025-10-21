start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

if start < end:
  print ("leap years between",start," and " ,end, ":")

while start < end:
    if start % 4 == 0 and start % 100 != 0 or start % 400 == 0:
        print(start)
        
    start += 1
    
     
   
