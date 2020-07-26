## Create a list based on user input
numofElem = int(input("Enter the number of elements"))

#Prepare the list element
iList = []
counter = 0
print("Number of elements",numofElem)
while counter <= numofElem:
    elem = int(input("Enter the element"))
    iList.append(elem)
    print(iList)
    counter = counter+1
    print(counter)

##Approach 1
trueFlag=False
pos=0
searchElem = int(input("Enter the element to be searched for"))
# for loopvar in iList:
#     if(loopvar == searchElem):
#         trueFlag=True
#         pos=iList.index(loopvar)
#         break
#     else:
#         falseFlag=False
#
# if(trueFlag==True):
#     print("Element",searchElem,"present in",iList,"at index",pos)
# else:
#     print("Element",searchElem,"not present in",iList)

##Approach 2
output=iList.count(searchElem)
if output == 0:
    print(searchElem,"not found in",iList)
else:
    print(searchElem,"found in",iList)