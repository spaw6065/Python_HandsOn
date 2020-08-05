def get_input(ptrn):
    print(ptrn)
    num1=int(input("Enter the number 1: "))
    num2 = int(input("Enter the number 2: "))
    operator=input("Enter the operation to be performed on the numbers: ")
    return num1,num2,operator

def ops_two_num(num1,num2,operator):
    if operator == "+":
        print("Selected choice is Add")
        return num1+num2
    elif operator == "-":
        print("Selected choice is Subtract")
        return num1-num2
    else:
        return -1

def ops_two_numv2(func,ptrn,operator):
    print("Entered ops_two_num")
    num1,num2,operator=func(ptrn)

    #print("function invoked",func)
    #expr=str(num1)+operator+str(num2)
    ##print("expression",int(expr))
    #print("type of expr",type(expr))

    if operator == "+":
        print("Selected choice is Add")
        return num1+num2
    elif operator == "-":
        print("Selected choice is Subtract")
        return num1-num2
    else:
        return -1

# x = get_input()
# print(x)
#
# print(ops_two_num(x[0],x[1],"+"))
# print(ops_two_num(x[0],x[1],"-"))

#print(ops_two_num(get_input()[0],get_input()[1],"+"))
pattern="---------------------------------------"
print(ops_two_numv2(get_input,pattern,"+"))