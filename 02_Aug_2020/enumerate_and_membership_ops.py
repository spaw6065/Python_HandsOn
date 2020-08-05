i_list = [10,1,11,9,4,99]
# for i in enumerate(range(4,8)):
#     print(i)

def custom_list_sort(m_list):
    temp_var = int()
    sorted_list = list()
    index = 0
    prev_small_value = int()
    for elem in m_list:
        ##custom sort
        print("------------------------")
        new_index = elem[0]
        #old_index = (elem[1])[0]
        value = (elem[1])[1]

        temp_var = value
        for elem2 in m_list:
            value2 = (elem2[1])[1]
            old_index = (elem2[1])[0]
            smallest_value = value2
            print("temp_var :",temp_var)
            print("value2 :",value2)
            print("old_index :",old_index)
            print("new_index: ",new_index)
            print("smallest_value : ",smallest_value)
            print("prev_small_value : ", prev_small_value)

            if (temp_var > value2 and
                value2 <= smallest_value and
                (smallest_value < prev_small_value
                 or prev_small_value ==0) ):
                smallest_value = value2
                preserve_index = old_index
                sorted_list.append((index,(old_index,smallest_value)))
                prev_small_value = smallest_value
                index += 1
                break;

        print("Sorted List",sorted_list)
        # print(elem[0][0][1])
        # print(elem[0][0][1][0])
        # print(elem[0][0][1][1])
        print("------------------------")

i_listmod = list()
##unsorted list with enumerate
for i in enumerate(i_list):
    print(i)
    i_listmod.append(i)
    i_listmod.sort()

print("Unsorted index",i_listmod)
print("-------------------------")

modified_list = list()
#sorted list with enumerate
for i in enumerate(i_listmod):
    modified_list.append(i)
print(modified_list)

print("Invoke custom sort")
custom_list_sort(modified_list)

