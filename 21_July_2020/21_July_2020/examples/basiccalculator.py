from examples import utils

choice = int(input("Enter choice"))

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

if(choice == 1):
    print(utils.add(num1,num2))
elif(choice == 2):
    print(utils.subtract(num1,num2))
elif(choice ==3):
    print(utils.multiply(num1,num2))
elif(choice == 4):
    print(utils.divide(num1,num2))
else:
    print("Enter a valid choice 1/2/3/4")
