# Enter your code here. Read input from STDIN. Print output to STDOUT
no_elements = int(input())
#print(no_elements)

def is_pallindrome(x):
    new_num = int()
    actual_num = x
    while x > 0:
        digit=x%10
        x  = x//10
        
        new_num = new_num*10+digit
        #print("new_num",new_num)
    if actual_num == new_num:
        #print("A",True)
        return(True)
    else:
        #print("B",False)
        return(False)


i_list = input().split()
i_TrueList = list()
if no_elements==1 and (int(i_list[0]) > 0 and is_pallindrome(int(i_list[0]))==True):
    print(True)
elif no_elements > 1:
    #print(i_list)
    for x in i_list:
        #print(x)
        y = int(x)

        condition_true=False
        #print(y)
        if y > 0:
            if is_pallindrome(y):
                #print("y True",y)
                #print(True)
                i_TrueList.append(True)
            else:
                pass
        else:
            #print("y False",y)
            i_TrueList.append(False)
    
    if all(i_TrueList):
        print(True)
    else:
        print(False)
else:
    print(False)




###
Solution 2
N,n = int(raw_input()),raw_input().split()
print all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n])


Solution 3
_, values = raw_input(), map(list, raw_input().split())
print(any([i==i[::-1] for i in values if all(["-" not in n for n in values])]))