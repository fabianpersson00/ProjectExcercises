"""
**Prime Factorization** - Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""

InputNumber = int(input())
ListofPrimeFactors = []

def CheckForPrime(IntToCheck):
    if IntToCheck == 0 or IntToCheck == 1:
        print("0 and 1 are not factorial numbers")
    else:
        for x in range(2, int(IntToCheck+1)):
            if (IntToCheck % x) == 0:
                ListofPrimeFactors.append(x)
                if (IntToCheck/x) != 1:
                    CheckForPrime(IntToCheck/x)
                break
CheckForPrime(InputNumber)
if len(ListofPrimeFactors) >= 1:
    print(ListofPrimeFactors)
