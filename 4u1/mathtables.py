# mini project (program for math tables)

n=int(input("enter a number from 0-10 :"))
print("Multiplication  table for", n ,"is:")
print("------------------------------------")
for i in range(1,11):
    print(n, "X",i,"=",n*i)
print("--------------------------------------")    