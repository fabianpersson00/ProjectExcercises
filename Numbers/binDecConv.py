'''
**Binary to Decimal and Back Converter**
-
Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
'''
import math
"Divide the number into two new numbers. One for being above or euqal to 1, and one for being less than 1."

binDec = str(input("Reply if you want to convert a bin to dec with 'bin', or with 'dec' if it's the other way around.: "))
binConv = False

if binDec == 'bin':
    binConv = True

while True:
    try:
        number = float(input("Input the number to be converted: "))
        break
    except ValueError:
        print("Wrong value for input. Retry.")

"ONLY TO FIX A ROUNDING BUG WITH FLOATS"
countDecimals = str(number).split(".")
lenDecimals = len(countDecimals[1])
largeSegment = math.floor(number)
smallSegment = round((number - largeSegment), lenDecimals)

baseOfTwo = []
decimalNumber = 0.0

if binConv:
    largeSegmentList = [char for char in str(largeSegment)]
    largeSegmentList.reverse()
    smallSegmentList = [char for char in str(smallSegment)]

    """Popping twice to the remove '0' and the ',' from the list."""
    smallSegmentList.pop(0)
    smallSegmentList.pop(0)
    print(largeSegmentList, smallSegmentList)
    exponent = 0
    for x in largeSegmentList:
        if x == '1':
            decimalNumber += 2**exponent
        exponent += 1
    
    exponent = 1
    for x in smallSegmentList:
        if x == '1':
            decimalNumber += (1/2**exponent)
        exponent += 1
    
    print(decimalNumber)
    
else:
    while largeSegment > 0:
        if largeSegment % 2 == 0:
            baseOfTwo.append(0)
            largeSegment = largeSegment/2
        else: 
            baseOfTwo.append(1)
            largeSegment = math.floor(largeSegment/2)
    baseOfTwo.reverse()
    baseOfTwoLargeString = "".join(map(str, baseOfTwo))
    baseOfTwo.clear()

    """Again, some weird rounding is happening with floats, like .321, is being rounded to .3200000075."""
    while smallSegment > 0 and len(baseOfTwo) < (lenDecimals**2):
        smallSegment *= 2
        smallSegment = round(smallSegment, lenDecimals)
        if smallSegment >= 1:
            baseOfTwo.append(1)
            smallSegment -= 1
            smallSegment = round(smallSegment, lenDecimals)
        else:
            baseOfTwo.append(0)
    baseOfTwoSmallString = "".join(map(str, baseOfTwo))
    convertedNumber = baseOfTwoLargeString + "." + baseOfTwoSmallString
    print(convertedNumber)

