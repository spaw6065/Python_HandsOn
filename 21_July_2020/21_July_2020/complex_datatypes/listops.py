ilist=["apple","banana","cherry","duck","eagle"]


#list operations
print(ilist)
print("length of the list is",len(ilist))
index = int(input("Enter the index element"))
try:
    if(index <= len(ilist)):
        print("Element at index ",ilist[index])
    else:
        print("Index is not proper")
except IndexError:
    print("Index out of range error")
finally:
    print("Check the error if any")

print(ilist[-4:-2])

ilist[3]="dogfood"
print(ilist)

# find the maximum length element in the list
maxlen = 0
index = 0
for x in ilist:
    length=len(x)
    if(length > maxlen):
        maxlen=length
        index += 1
    else:
        pass

print("maximum length of the element in the list",ilist,"is",maxlen,"and element is",ilist[index])

## operations on list using built in methods
print("-------------------------------------")
ilist.remove("banana")
print(ilist)

ilist.append("cat")
print(ilist)

del(ilist[0])
print(ilist)

ilist2 = [1,2,3,4,5]
ilist.extend(ilist2)
print(ilist)

print(ilist.count(6))

print(ilist.index(5))

ilist3 = ilist.copy()
ilist.pop()
print(ilist3)
print(ilist)