#12. Write a Python program to find sum of first and last digit of a number.
input_number = int(input("Enter the number:"))
fmt_str = "Number : {0} \n".format(input_number)

first_digit = int()
last_digit = int()

def get_firstlast_digit(inp_num):
    NoofDigits = 0


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

    #print("first_digit:",first_digit)
    #print("last_digit:",last_digit)

    return first_digit,last_digit

def reverse_digits(input_number,first_digit,last_digit):
    new_number = int()

    while (input_number != 0):
        digit = input_number%10
        input_number = input_number//10
        new_number = new_number*10+digit
    return new_number

def swap_firstlastdigit(input_number,first_digit,last_digit):
    numtostr = str(input_number)
    #TODO : Used
    # newstr = numtostr.replace(numtostr[0],last_digit)
    # finalstr = newstr.replace(newstr[len(newstr)-1,first_digit)
    #return(finalstr)
    #TODO : How to swap first and last digits keeping middle digits intact

def is_pallindrome(input_num,reverse_num):
    if input_num == reverse_num:
        return True
    else:
        return False


f_digit,l_digit = get_firstlast_digit(input_number)
rev_num = reverse_digits(input_number,first_digit,last_digit)
#flswap_num = swap_firstlastdigit(input_number,first_digit,last_digit)
swap_firstlastdigit(input_number,f_digit,l_digit)

isPallindrome = is_pallindrome(input_number,rev_num)

print(fmt_str+
          "first digit {0} \n" 
          "last digit {1} \n"
          "their sum is {2} \n"
          "reverse num is {3} \n"
          "and is Pallindrome {4} \n"
          "first and last digit swapped number is {0} ".format(f_digit,
                                                               l_digit,
                                                               l_digit+l_digit,
                                                               rev_num,
                                                               isPallindrome))





