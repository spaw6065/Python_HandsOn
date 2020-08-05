import math
import random
inp = int(input("Guess the number between 1 and 100"))

actual_num = random.randint(1,100)
actual_num2 = random.randrange(0,100)
# print(actual_num)
# print(actual_num2)

no_of_chances = 0

while True:
    if inp > actual_num:
        inp = int(input("Enter a lower number"))
        no_of_chances += 1
    elif inp < actual_num:
        inp = int(input("Enter a higher number"))
        no_of_chances += 1
    else:
        print(f"Bingo, You{chr(32)}made the right guess.\nThe number is {actual_num} and your guess is {inp} after {no_of_chances} chances...")
        break

