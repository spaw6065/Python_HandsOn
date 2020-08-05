#5) WAP to find the duplicate and unique elements in a list.
#example: list1 = [1,2,3,4,5,6,2,3,4,5,6,8]

ilist = [1,2,3,4,5,6,2,3,4,5,6,8]
unique_elem_list = list()
dup_elem_list = list()


for x in ilist:
    if ilist.count(x) >= 2 and x not in dup_elem_list:
        dup_elem_list.append(x)
    elif ilist.count(x) == 1:
        unique_elem_list.append(x)
    else:
        pass

print("Duplicate elements in the list ",dup_elem_list)
print("unique elements in the list ",unique_elem_list)