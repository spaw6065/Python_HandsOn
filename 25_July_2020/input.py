##Program to add two numbers
import math as m

# num1 = int(input("Enter number 1 "))
# print(type(num1))
# print(isinstance(num1,str))
# num2 = int(input("Enter number 2 "))
#
# sum = num1+num2
# print("Sum is",sum)

print("---------------------")
s="10.5"

print(id(s))
print("original address" ,id(s))
s1=float(s)

print(type(s1))
print("new address ",id(float(s)))
print(id(s))
if(s == (float(s))):
    print("Yes")
else:
    print("No")

print("s1",s1)

print(m.trunc(2.666))

print(py4j.version)