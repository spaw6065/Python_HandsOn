#19. Write a Python program to find power of 2 for number 1 to n using loop.
#ask user to enter value of n


inp_cnt = int(input("Enter the value of nth number starting from 1"))

for x in range(1,inp_cnt):
    print("number : {0} and pow(2) :{1}".format(x,x**2))
