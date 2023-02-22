dn=int(input("Enter a number:"))
bn=0
i=0
while dn!=0:
    r=dn%2
    bn=bn+r*(10**i)
    bn=dn//2
    i+=1
print(bn)    