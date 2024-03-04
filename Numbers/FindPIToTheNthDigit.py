"""**Find PI to the Nth Digit**
Enter a number and have the program generate PI up to that many decimal places. 
Keep a limit to how far the program will go."""

import math

print("Enter a number and I will return PI to the Nth number.")
NthDigit = int(input())
if (NthDigit <= 15):
    NumberPi = str(math.pi)
    NthPi = NumberPi[:(NthDigit+2)]
    print(NthPi)
else:
    print("Too many decimals, please go below 15.")