'''6) WAP to create a Fibonacci series of n numbers.
# 0,1,1,2,3,5,8….'''

input_num = int(input("Enter the number till printing the fibonacci series"))

first_num = 0
next_num = 1
cntr = 1
print(first_num,end=" ")
while cntr <= input_num:
    first_num,next_num=first_num+next_num,first_num
    print(first_num,end=" ")
    cntr += 1