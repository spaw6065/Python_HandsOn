#17 WAP to lower the string
##Approach #1
str1 = input("Enter the string")
lower_str = str()
for x in str1:
    lower_str += x.lower()

print("Original String {0} and lower case string {1}".format(str1,lower_str))

##Approach #2
print("Original String {0} and lower case string {1}".format(str1,str1.lower()))