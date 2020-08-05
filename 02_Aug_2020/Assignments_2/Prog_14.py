#14) WAP to reverse a string
str1 = input("Enter the string")

##Approach #1
newStr = str()
cntr = len(str1)
while cntr != 0:
    newStr += str1[cntr-1]
    cntr -= 1

print(f"actual string {str1} and reversed string {newStr}")

