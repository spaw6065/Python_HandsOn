##left half pyramid
inp = int(input("Enter the counter value"))

print("Left hand triangle")
for x in range(0,inp):

    for y in range(0,inp):
        if x >= y:
            print("* ",end="")
        else:
            print(end="")
    print(" ")

# print("------------------------")
# print("right half pyramid")
# for x in range(0,inp):
#
#     for y in range(x,inp):
#             print("*",end="")
#     print()

# #inp = int(input("enter the value of pattern: "))
# print("left side triangle")
# for i in range(0,inp):
#     for j in range(0,inp):
#         if i+j < inp:
#             print("*",end=" ")
#
#     print("\t")
#
# print("--------------------------")
# #inp = int(input("enter the value of pattern: "))
#
# ##right side triangle
print("Right side triangle")
for i in range(0,inp):
    for x in range(0,inp-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print("\t")

# ##pyramid
print("----------------------------")
print("pyramid")
n=inp
for i in range(0,inp):
    for k in range(0,n+1):
        print(end=" ")
    n=n-1
    for j in range(0,i+1):
        print("*",end="")
        print(end=" ")

    print("\t")

print("----------------------")
print("Inverse pyramid")
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
n=inp
for i in range(0,inp):
    for j in range(0,i+1):
        print(end=" ")
    for k in range(0,n):
        print("*",end=" ")
    n=n-1
    print()

print("----------------------")
print("Right star")
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
n = inp
for x in range(0,inp):
    for y in range(0,x+1):
        print("*",end=" ")
    print()

for x in range(1, n):
    for y in range(1,n):
        print("*",end=" ")
    n = n-1
    print()


print("Hour glass pyramid")
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
n = inp
m = inp
for x in range(0,inp):
    for k in range(0,x+1):
        print(" ",end="")
    for y in range(0,n):
        print("*",end=" ")
    n = n-1
    print()
for x in range(1,inp):
    for k in range(0,m-1):
        print(" ",end="")

    for y in range(0,x+1):
        print("*",end=" ")
    m = m-1
    print(" ", end="")
    print()

print("--------------------------------")
print("Diamond")
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
n = inp
m = inp
for x in range(0,inp):
    for k in range(0,m-1):
        print(" ",end="")

    for y in range(0,x+1):
        print("*",end=" ")
    m = m-1
    print(" ", end="")
    print()
for x in range(0,inp):
    for k in range(0,x+1):
        print(" ",end="")
    for y in range(1,n):
        print("*",end=" ")
    n = n-1
    print()