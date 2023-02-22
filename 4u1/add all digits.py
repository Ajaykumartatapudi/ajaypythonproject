#to add all the digits in a number.
n=int(input("Enter A Number:"))
i=s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print(s)    