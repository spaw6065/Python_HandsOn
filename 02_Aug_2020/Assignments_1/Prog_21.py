#21) Write a Python program to print all Prime numbers between 1 to n.

def is_prime(inp_num):
    if (inp_num in [1, 2, 3, 5, 7]):
        print(inp_num,end=" ")
    elif (inp_num % 2 != 0 and inp_num % 3 != 0 and inp_num % 5 != 0 and inp_num % 7 != 0):
        print(inp_num,end=" ")
    else:
        #print("input number {0} is not prime".format(inp_num))
        pass


inp_cnt = int(input("Enter the nth element of the range of elements"))

for x in range(1,inp_cnt):
    is_prime(x)