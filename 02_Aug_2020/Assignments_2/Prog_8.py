##8) WAP to find the first hundred prime numbers.

input_num = int(input("Enter the number"))

def is_prime(input_num):
    if input_num in [1,2,3,5,7]:
        return 1
    elif input_num%2 == 0 or input_num%3 == 0 or input_num%5 ==0 or input_num%7==0:
        return 0
    else:
        return 1



isPrime = is_prime(input_num)
if isPrime:
    print(f"Entered number {input_num} is Prime")
else:
    print(f"Entered number {input_num} is not Prime")