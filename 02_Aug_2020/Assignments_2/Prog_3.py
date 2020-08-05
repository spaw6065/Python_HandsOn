'''3) WAP to get the basic salary from employee and
calculate it gross salary (Basic salary + 10% DA
and 12%TA)'''

basic_sal = int(input("Enter the basic salary for the employee... "))

DA = int(.10*basic_sal)
TA = int(.12*basic_sal)
gross_sal = basic_sal + DA+TA

print(f"Basic salary is {basic_sal} \u20B9 and Gross salary is {gross_sal} \u20B9")