##20. Write a Python program to check whether a number is Prime number or not
inp_num = int(input("Enter the number"))

if (inp_num in [1,2,3,5,7]):
    print("input number {0} is prime".format(inp_num))
elif (inp_num%2 != 0 and inp_num%3 != 0 and inp_num%5 != 0 and inp_num%7 != 0):
    print("input number {0} is prime ".format(inp_num))
else:
    print("input number {0} is not prime".format(inp_num))