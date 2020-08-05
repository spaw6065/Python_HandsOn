##7) WAP to get the factorial of user defined number.
inp_num = int(input("Enter the number..."))

def factorial(input_num):
    if input_num == 1:
        return 1
    else:
        return input_num*factorial(input_num-1)


factorial_val = factorial(inp_num)
print(f"Entered number is {inp_num} and factorial is {factorial_val}")