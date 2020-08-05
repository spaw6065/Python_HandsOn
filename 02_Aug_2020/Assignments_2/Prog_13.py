'''13) WAP to reverse/inverse key:value like below.
#dict1 = {‘a’: 1, 'b':2}
#Expected result: dict2 = {1: 'a', 2: ‘b’}'''

dict1 = {'a':1,
         'b':2,
         'c':3}

reverse_dict = dict()
for x in dict1:
    reverse_dict[dict1[x]] = x

print(reverse_dict)

