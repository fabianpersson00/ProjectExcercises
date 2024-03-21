'''
**Change Return Program** 
- 
The user enters a cost and then the amount of money given. 
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
'''
import math

while True:
    try:
        cost = float(input("Enter the cost of the product: "))
        break
    except ValueError:
        print("Input is not correct. Retry")

while True:
    try:
        paidMoney = float(input("Enter the money given for said product: "))
        break
    except ValueError:
        print("Input is not correct. Retry")

money = dict({"quarters":0.25, "dimes":0.1, "nickels":0.05, "pennies":0.01})

if (paidMoney < cost):
    print("You paid to little...")
else:
    diffMoney = paidMoney - cost
    
    amountOfQuarters = math.floor(diffMoney//money["quarters"])
    diffMoney -= amountOfQuarters * money["quarters"]

    amountOfDimes = math.floor(diffMoney//money["dimes"])
    diffMoney -= amountOfDimes * money["dimes"]

    amountOfNickels = math.floor(diffMoney//money["nickels"])
    diffMoney -= amountOfNickels * money["nickels"]

    amountOfPennies = math.floor(diffMoney//money["pennies"])
    diffMoney -= amountOfPennies * money["pennies"]

    print("You will get back ", amountOfQuarters, " quarters, ", amountOfDimes, " dimes, ", amountOfNickels, " nickels, ", amountOfPennies, " pennies.")