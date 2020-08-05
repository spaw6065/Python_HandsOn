#16) WAP to split the string and store only even placed items in list
str1 = input("Enter the string")

##Approach #1
iListStr = str1.split()

iListStr2 = list()
##Approach # 2
split_sep = " "
x = 0
prev_sep_pos = 0

while x < len(str1):
    print(x)
    if str1[x] == split_sep:
        word = str1[prev_sep_pos:x]
        prev_sep_pos = x
        #print(f"space separator {prev_sep_pos}")
        #print(f"word : {word}")
        iListStr2.append(word)
    x = x+1

iListStr2.append(str1[prev_sep_pos:len(str1)])

print(f"String {str1} and list {iListStr2}")