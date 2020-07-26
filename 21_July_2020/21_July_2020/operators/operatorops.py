#arithmetic operators
num1 = 20
num2 = 2

print(num1/num2)
print(num1//num2)
print(num1%num2)
print(num1**2)

print("num1:",num1)
print("num2:",num2)
#comparison operators
if not(num1 != num2):
    print("num1 and num2 are not equal")
elif(num1 > num2):
     print("num1 is greater than num2")
else:
    print("num is less than num2")

#identity operators
if num1 is num2:
    print("True")
else:
    print("False")


#membership operators
if num2 is num1:
    print("is member of")
else:
    print("is not a member of")