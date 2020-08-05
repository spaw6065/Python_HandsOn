#1. Print natural number from 1 to n
n_range = int(input("Enter the value of last nth number:"))
print("1 to n".center(50,"*"))
for x in (range(0,n_range+1)):
    print(x)

#2. Write a Python program to print all natural numbers in reverse
# (from n to 1).
print("Reverse from n to 1".center(50,"*"))
i_list = list()
for x  in range(0,n_range+1):
    i_list.append(x)
print(i_list)
i_list.sort(reverse=True)
print(i_list)

#3. Write a Python program to print all alphabets from a to z.
print("a to z ".center(50,"*"))
for asciivalue in range(97,123):
    print(chr(asciivalue),end=" ")

#4. Write a Python program to print all even numbers between 1 to 100.
print()
print("EVEN numbers".center(50,"*"))
for x in range(1,101):
    if x%2 == 0:
        print(x,end=" ")
    else:
        pass

#5. Write a Python program to print all odd number between 1 to 100
print()
print("ODD Numbers".center(50,"*"))
for x in range(1,101):
    if x%2 != 0:
        print(x,end=" ")
    else:
        pass

#6. Write a Python program to find sum of all natural numbers between 1 to n.
print("sum of 1 to n".center(50,"*"))
sum = 0
for x in (range(0,n_range+1)):
    sum = sum+x
print("Sum from {0} to {1} is {2}".format(0,n_range,sum))

#7. Write a Python program to find sum of all even numbers between 1 to n.
print()
even_sum = 0
print("EVEN numbers Sum".center(50,"*"))
for x in range(1,n_range):
    if x%2 == 0:
        even_sum = even_sum+x
    else:
        pass
print("Sum of even numbers between {0} and {1} is {2}".format(0,n_range,even_sum))

#8. Write a Python program to find sum of all odd numbers between 1 to n.
print()
odd_sum = 0
print("ODD numbers Sum".center(50,"*"))
for x in range(1,n_range):
    if x%2 != 0:
        odd_sum = odd_sum+x
    else:
        pass
print("Sum of even numbers between {0} and {1} is {2}".format(0,n_range,odd_sum))

#9. Write a Python program to print multiplication table of any number.
tableOf_Num = int(input("Enter the number to print the table for:"))
for x in range(1,11):
    print("{0} * {1} = {2}".format(tableOf_Num,x,tableOf_Num*x))

#10. Write a Python program to count number of digits in a number.
number1 = int(input("Enter the number"))
print("Number of digits present in {0} is {1}".format(number1,len(str(number1))))






