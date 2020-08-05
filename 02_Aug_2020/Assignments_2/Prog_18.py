#18) S="EtHaNs", swap the cases in the word "eThAnS";
##Approach #1
str1 = input("Enter the string")
print("Swapped case ",str1.swapcase())
newStr = str()

##Approach # 2
for x in str1:
    if x.isupper():
        newStr += x.lower()
    elif x.islower():
        newStr += x.upper()
    else:
        pass
print("old string {0} and new string {1}".format(str1,newStr))