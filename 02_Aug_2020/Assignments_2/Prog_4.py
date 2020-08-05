#4) WAP to reverse a given number.
inp_num = int(input("Enter the number"))

def reverse_num(inp_num):
    new_num=0
    while inp_num > 0:
        digit = inp_num%10
        inp_num = inp_num//10
        new_num = new_num*10+digit

    return new_num

print(f"Entered number {inp_num} and reverse number is {reverse_num(inp_num)}")