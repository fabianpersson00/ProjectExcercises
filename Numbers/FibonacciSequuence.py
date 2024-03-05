"""
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""
num1, num2 = 0, 1

NthNumber = int(input())
print("Fibonacci Sequence:")
if NthNumber >= 1:
    print(str(num1))
    if NthNumber >= 2:
        print(str(num2))
        if(NthNumber > 2):
            for x in range(NthNumber-2):
                sum = num1 + num2
                print(str(sum))
                num1 = num2
                num2 = sum
else:
    print("Something has gone wrong here")
print("Finished!")