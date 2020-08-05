for i in range(0,10):
    print("i ",i)

print('------------------------------------')
i_list = [0,2,3,4,5,6,7,8,9]
for counter in i_list:
    print(counter)

print('------------------------------------')
i_list.append(1)
i_list.sort()
print(i_list)

print('------------------------------------')
i_list2=list()
for i in range(10,0,-1):
    print(i,end=",")
    i_list2.append(i)


print()
print(i_list2)

print('------------------------------------')
idNameList  = ["id",101,"name","Sumit"]
dict1 = dict()
index_value = 0
for elem in idNameList:
    for index_value in range(0,len(idNameList)):
        if index_value%2==0:
            dict1[idNameList[index_value]]=idNameList[index_value+1]
print(dict1.keys())

print('------------------------------------')
str1 = "This is Python Class"

print("End")

print('------------------------------------')
#i_list3 = [1,2,3,4,5,6,7,8,9,10]
start_elem = int(input("Enter the range start number"))
end_elem = int(input("Enter the range end number"))

i_list4 = range(start_elem,end_elem)
even_list=list()
odd_list=list()

for cntr in i_list4:
    if cntr%2==0:
        even_list.append(cntr)
    else:
        odd_list.append(cntr)

print("Even numbers count",len(even_list))
print("Odd numbers count",len(odd_list))

print('------------------------------------')
##Identify total number of classes on each day
days=["Sun","Mon","Tue","Wed","Thurs","Fri","Sat"]
batches = ["First","Second","Third"]

print("Total number of batches",len(days)*len(batches))

i_list = list()
for day in days:
    day_cnt = 0
    for batch in range(0,len(batches)):
        print(f"{day} and batch {batches[batch]}")

    print("----------------------------------")
print('---------------------------------------------')

print(dict1.keys())
print(dict1.values())
print(dict1.items())
output_fmt = "{0}--->{1}"
for key,value in dict1.items():
    print(output_fmt.format(key,value))