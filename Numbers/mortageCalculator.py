'''
Mortgage Calculator
- 
Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
Also figure out how long it will take the user to pay back the loan. 

For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

Formula: payment = loan * (interrest rate / amount of payments anually)
Interrest rate always assumed to be 6%.
'''
import re

print("Please input the loan, and type of payment, and the term (always assumed in years). Ex: '450000, monthly, 5'")
interestRate = 0.06
amountInterval = str(input())

amountInterval = re.split(", ", amountInterval)
intervalFloat = 0
intervalString = "interval"
loan = float(amountInterval[0])
interval = amountInterval[1]
term = float(amountInterval[2])
if interval == 'monthly':
    intervalFloat = 12
    intervalString = "months"
elif interval == 'weekly':
    intervalFloat = 52
    intervalString = "weeks"
elif interval == 'daily':
    intervalFloat = 365
    intervalString = "days"
else:
    print("Something has gone wrong")

intervalPayment = loan * interestRate / intervalFloat
print("Your payment comes to", intervalPayment, "$ per interval.")

intervalsToComplete = loan / intervalPayment
print("You'll be completing this mortage payment in", intervalsToComplete, intervalString)

leftOfLoan = loan - (loan * interestRate * term)
print("After the term you will still owe another", leftOfLoan, "$ to the bank")
