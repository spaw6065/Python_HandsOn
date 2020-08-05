##9) WAP to accept three inputs from the user and find the greatest number
##among 3 numbers.

cntr = 0
inp_num = list()

def sum_three_numbers(input_num):
    num1 = int(input_num[0])
    num2 = int(input_num[1])
    num3 = int(input_num[2])
    return num1+num2+num3


while cntr < 3:
    inp_num.append(input(f"Enter the number {cntr+1}"))
    cntr += 1

print(f"You have entered num1 : {inp_num[0]} "
      f"num2 : {inp_num[1]} "
      f"num3 : {inp_num[2]} "
      f"and their sum is {sum_three_numbers(inp_num)}")


