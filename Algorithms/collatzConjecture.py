'''
**Collatz Conjecture**
- 
Start with a number *n > 1*. 
Find the number of steps it takes to reach one using the following process:
If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1.

'''

while True:
    try:
        numberN = int(input("Input a positive integer: "))
        break
    except ValueError:
        print("Wrong type, please recheck your input")

listTrail = []

while numberN != 1:
    listTrail.append(int(numberN))
    if (numberN % 2) == 0:
        numberN = numberN / 2
    else:
        numberN = (numberN * 3) + 1

print("Took", len(listTrail),"iterations to get to 1. See list below for all numbers in the step.")
print(listTrail)
