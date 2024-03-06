"""
**Prime Factorization** - Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""
InputNumber = int(input())

def CheckForPrime(IntToCheck, DivBy = 2):
    ListOfPrimes = []
    IntToCheck
    if IntToCheck == 0 or IntToCheck == 1:
        print("0 and 1 are not factorial numbers")
        return
    else:
        while (IntToCheck % DivBy == 0):
            ListOfPrimes.append(DivBy)
            IntToCheck = IntToCheck/DivBy
        if (IntToCheck == 1):
            return ListOfPrimes
        else:
            ListOfPrimes = ListOfPrimes + CheckForPrime(IntToCheck, (DivBy+1))
            return ListOfPrimes
    
print(CheckForPrime(InputNumber))
