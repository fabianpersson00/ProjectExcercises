"""
Enter a number and have the program generate e up to that many decimal places. 
Keep a limit to how far the program will go.
"""

import math

StringOfE = str(math.e)
NthDecimal = int(input())

if(NthDecimal <= 15):
    print(StringOfE[:(NthDecimal+2)])
else:
    print("Too many decimals, please only input a maximum of 15.")
