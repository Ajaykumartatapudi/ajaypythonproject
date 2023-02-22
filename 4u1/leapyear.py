a=int(input("enter a value"))
if(a%4==0):
    if(a%100==0):
       if(a%400==0):
           print("given year is leap year")
       else:
           print("given year is not leap year")
    else:
        print("given year is leap year")
else:
    print("given year is not leap year")
    
        
        
