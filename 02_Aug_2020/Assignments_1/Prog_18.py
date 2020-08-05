#18. Write a Python program to find frequency of each digit in a given integer.
inp_num = int(input("Enter the number:"))
copy_inp_num = inp_num
fmt_str = "Number : {0} ".format(inp_num)

NoofDigits = 0
i_list = list()

while (inp_num != 0):
    #print("inp_num:",inp_num)

    #print("-----------------")
    digit = inp_num%10
    NoofDigits += 1
    inp_num = inp_num // 10
    i_list.append(digit)

    #print("digit :",digit)
    #print("NoofDigits:", NoofDigits)
    #print("-----------------")

for x in i_list:
    print("digit {0} is repeated {1} times in the number {2}".format(x,i_list.count(x),copy_inp_num))
# print(fmt_str+
#       "and their individual digit frequency ".format())



