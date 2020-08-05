#12. Write a Python program to find sum of first and last digit of a number.
inp_num = int(input("Enter the number:"))
fmt_str = "Number : {0} ".format(inp_num)

NoofDigits = 0
first_digit = int()
last_digit = int()

while (inp_num != 0):
    #print("inp_num:",inp_num)

    #print("-----------------")
    digit = inp_num%10
    NoofDigits += 1
    inp_num = inp_num // 10


    if(NoofDigits == 1):
        last_digit = digit
    elif(inp_num == 0):
        first_digit = digit
    else:
        pass

    #print("digit :",digit)
    #print("NoofDigits:", NoofDigits)
    #print("-----------------")

print("first_digit:",first_digit)
print("last_digit:",last_digit)
print(fmt_str+
      "first digit {0} " 
      "last digit {1} "
      "and their sum is {2} ".format(first_digit,last_digit,first_digit+last_digit))



