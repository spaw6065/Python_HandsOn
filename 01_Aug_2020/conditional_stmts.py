str1= input("Enter the value separated by ")
values= str1.split(",")
print(values)

if (values[0].isdigit() and values[1].isdigit()):
    print("You have entered digits")
    sum = int(values[0])+int(values[1])
    print("sum : ", sum)
elif values[0].isalpha() and values[1].isalpha():
    print("You have entered string")
    concatString = values[0]+" "+(values[1])
    print("concatenated string: ",concatString)
else:
    print("Alphanumeric not supported")

