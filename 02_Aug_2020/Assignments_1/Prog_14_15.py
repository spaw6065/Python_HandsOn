#14. Write a Python program to find the sum of the digits of number and the product of the digits of the number
inp_num = int(input("Enter the number:"))
fmt_str = "Number : {0} ".format(inp_num)

NoofDigits = 0
digit_sum = 0
digit_prod = 1
while (inp_num != 0):
    #print("inp_num:",inp_num)

    #print("-----------------")
    digit = inp_num%10
    NoofDigits += 1
    inp_num = inp_num // 10

    digit_sum = digit_sum  + digit
    digit_prod = digit_prod * digit
    #print("digit :",digit)
    #print("NoofDigits:", NoofDigits)
    #print("-----------------")

print(fmt_str+
      "and their digit sum is {0} "
      "and their digit product is {1} ".format(digit_sum,digit_prod))



