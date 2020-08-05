str = input("Enter the string")
fmt="***{0}***"
print(fmt.format(str))
print(str.center(len(str)+6,"*"))