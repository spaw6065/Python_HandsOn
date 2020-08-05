tuple1 = (12,2,23,14,1)
print(tuple1)
# print(tuple1.index("sumit"))
#
# print(tuple1.count("sumit"))


iList4=[22,2,3,4,5,6,7,8,9,10]
iList4.sort()
print("Sort ASC",iList4)

iList4.sort(reverse=True)
print("Sort DSC", iList4)

tuple1 = (12,2,23,14,1)
tupleToList = list(tuple1)

print(type(tupleToList))
print("unsorted :", tupleToList)
tupleToList.sort(reverse=True)

print("Sorted List", tupleToList)
print("Sorted Tuple", tuple(tupleToList))

tuple3 = tuple(iList4)
print("tuple3", tuple3)




