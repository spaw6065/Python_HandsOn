##tuple operations
tuple1 = ("india","china","Nepal")

print(tuple1)
str1= ""
for index in tuple1:
    str1 = str1 + "," + index
print(type(str1))
print(type(tuple1))

##range ops
print(tuple1[-1:])
print(tuple1[1:2])

list1=list(tuple1)
print("List",list1)

list1[1]="Pakistan"
tuple1=tuple(list1)
print(tuple1)

