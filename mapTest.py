from functools import reduce
list1=[1,2,3,4,5,6,7,8,9]
#Map
tempList=list(map(lambda x:x**2,list1))
print(tempList)
#Filter
tempList1=list(filter(lambda x:x%2==1,list1))
print(tempList1)
#Reduce
sumList1=reduce(lambda x,y:x+y,list1)
print(sumList1)