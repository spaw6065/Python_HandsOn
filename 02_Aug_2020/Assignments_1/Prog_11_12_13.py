#11. Write a Python program to find first and last digit of a number.
number_1 = input("Enter the number:")
print("First digit of {0} is {1} and last digit is {2}".format(number_1,number_1[0],number_1[len(number_1)-1]))

#12. Write a Python program to find sum of first and last digit of a number.
print("First digit of {0} is {1} and last digit is {2} and sum is {3}".format(number_1,
                                                                              number_1[0],
                                                                              number_1[len(number_1)-1],
                                                                              (int(number_1[0])+int(number_1[len(number_1)-1]))))

#13. Write a Python program to swap first and last digits of a number.
#print("Swapping first and last digit of {0} will give {1}".format(number_1,))'
first_digit = number_1[0]
last_digit = number_1[len(number_1)-1]
print(first_digit)
print(last_digit)
print()


