num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

choice = int(input("Enter your guess"))

retryChoice=0

while (retryChoice != 3):
    if(choice >= num1 and choice <= num2):
        print("Winner")
        break
    else:
        print("Loser")
        choice = int(input("Enter your guess"))
    retryChoice +=  1
    #print(retryChoice)