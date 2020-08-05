iList=[1,2,3,4,5,6,7,8,9,10]

print(iList[0])
print(iList.append(11))
print(iList.pop(1))

print(iList)

l = [1,2,3,4,5,6,'ethans',[1,2,3,4]]
print(l.index(l[7].index(3)))

iList=[1,2,3,4,5,6,7,8,9,10]
iList2 = iList.copy()
print(id(iList[0]))
print(id(iList2[0]))

a = 10
b = 10
print(id(a))
print(id(b))


iList.insert(1,100)
print(id(iList))

#iList.clear()
print(id(iList))

iList4=[22,2,3,4,5,6,7,8,9,10]
print("Sort ASC", iList4.sort())
print("Sort DSC", iList4.sort(reverse=False))
