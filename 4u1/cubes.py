#to evaluate list of a cubes till the range of 10
#<..................cubes................>
cubes=[]
for i in range(11):
    cubes.append(i**3)
print(cubes)
#to find the sum and mean of series 0 to 10
#<..................Mean................>
abc=[1,2,3,4,5,6,7,8,9,10]
sum=0
for  i in abc:
    sum+=i
print("the sum of the list is:",sum)
print("the mean of the list is :",sum/len(abc))
#  max & min  value in list
#<................max & min value..............>
list=[90,0,8,7]
print(list)
print("The Maximum value is :",max(list))
print("The Minimum value is :",min(list))
#<..............sorting...............>
ab=[-0,-99,99,231,86]
x=sorted(ab)
print("stored list:",x)
ab.append(10)
ab.remove(0)
print(ab)
