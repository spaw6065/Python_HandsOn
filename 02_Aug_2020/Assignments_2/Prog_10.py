'''10) WAP to check whether the user input number is Prime, Armstrong number
and find out the ascii value of that number.'''

def is_armstrong(inp_num):
    ##123
    inp_num_copy = inp_num
    armstrong_num = 0
    while inp_num_copy != 0:
        digit = inp_num_copy%10
        inp_num_copy = inp_num_copy//10
        armstrong_num = armstrong_num + digit**3
    #print(f"armstrong_num : {armstrong_num} ")
    if inp_num == armstrong_num:
        return 1
    else:
        return 0


number_input = int(input("Enter the number"))
isArmstrong = is_armstrong(number_input)

#print(isArmstrong)
if isArmstrong == 1:
    print(f"You have entered {number_input} and it's armstrong number "
          f"it's ascii value is {ascii(number_input)}")
else:
    print(f"You have entered {number_input} and it's not armstrong number "
          f"it's ascii value is  {ascii(number_input)}")