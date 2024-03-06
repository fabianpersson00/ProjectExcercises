"""
**Next Prime Number** - Have the program find prime numbers until the user chooses to stop asking for the next one.
"""

print("Start by typing any character(s) and pressing 'Enter' to generate Prime Number starting from 2. For next prime type 'next', or if 'stop' to stop the program.")
input()

num = 2
divBy = 2
printPrime = True
while printPrime:
    if num%divBy == 0 and num == divBy:
        print("Prime: ", num)
        print("Do you wish to continue? Write 'next' or 'stop'")
        toContinue = str(input())
        if toContinue == "stop":
            printPrime = False
        else:
            num += 1
            divBy = 2
    else:
        if num % divBy == 0:
            num += 1
            divBy = 2
        else:
            divBy += 1
