##3. WAP to pay the bill at a restaurant
##-take base total as input from the user
##-take tax percent(10/20/30...) as input from user
import math

baseTotal = float(input("Enter the bill base amount"))
taxRate = float(input("Enter the tax rate"))
billAmount = 0
if baseTotal == 0:
    print("You have 0.0 $ bill")
else:
    billAmount = math.ceil(baseTotal + baseTotal*(taxRate/100))
    #print(round(baseTotal + baseTotal * (taxRate / 100), 2))
    print("billAmount ",billAmount)
