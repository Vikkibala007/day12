mylist = [[1,2,3],[5,6,7],[10,11,12]]
sumList = []
maxValueIndex=[]
for subList in mylist:
    sumList.append(sum(subList))
    maxValue = max(sumList)
    maxValueIndex = mylist.index(maxValue)
print(sumList)    
print(maxValue)
print(maxValueIndex)
