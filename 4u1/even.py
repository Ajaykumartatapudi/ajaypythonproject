n=int(input("Enter A Number:"))
i=s=k=0
while(i<=n):
    if(i%2==0):
        s=s+i
    elif(i%2!=0):
        k=k+i
    i=i+1
print(s,k)
