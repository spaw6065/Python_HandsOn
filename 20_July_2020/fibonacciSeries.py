## fibonacci series is 0 1 1 2 3 5 8 13 21 34

# Take input from user for printing the fibonacci series to a specific length
fib_len = int(input("Enter the length of fibonacci series"))

##Approach 1
current_elem = 0
next_elem = 1
print(current_elem)
counter = 0
print(range(fib_len))
for counter in range(fib_len):
    # 0 1 1 2 3 5
    print(next_elem) # 0 1
    prev_elem = next_elem # 1
    next_elem = current_elem + prev_elem # 1
    current_elem = prev_elem
    counter = counter+1

##Approach 2
counter2 = 0
current_elem2 = 0
next_elem2 = 1
for counter2 in range(fib_len):
    print(current_elem2)
    current_elem2,next_elem2=next_elem2,current_elem2+next_elem2