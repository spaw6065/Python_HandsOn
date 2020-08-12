def ispallindrome(num):
    num_copy = num
    #print("num_copy",num_copy)
    reverse_num = int()
    while num > 0:
        digit = num%10
        num = num // 10
        reverse_num = reverse_num*10+digit

    if num_copy == reverse_num:
        #print("p if")
        return True
        ##yield num_copy
    else:
        #print("p else")
        ##pass
        return False

def check_infinites(input_num):
    cntr = 0
    while True:
        #print(f"input num {input_num}")
        listpallindrome = ispallindrome(input_num)
        if listpallindrome:
            number = (yield input_num)

        #if cntr==5:
            #print("if")
        #    break
        #else:
            #print("else")
        #    pass
        #cntr += 1
        input_num += 1

if __name__ == "__main__":
    print("From main")
    input_num=int(input("Enter the number"))
    print(ispallindrome(input_num))
##print(f"input number {input_num} is pallindrome: {ispallindromeFlag} ")
