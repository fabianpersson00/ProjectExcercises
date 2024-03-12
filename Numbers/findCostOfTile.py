'''
Find Cost of Tile to Cover W x H Floor
-
Calculate the total cost of tile it would take to cover a floor plan of width and height, 
using a cost entered by the user.
'''

import re

print("Please input WxH and then the price per unit seperated by a coma. Example: '2x3, 14'")

whPrice = str(input())
whPrice = re.sub("\s", "", whPrice)
whPrice = re.sub("x", ",", whPrice)
whPrice = re.split(",", whPrice)

width = int(whPrice[0])
height = int(whPrice[1])
price = int(whPrice[2])

totalCost = width * height * price

print("The total cost for this would be:", totalCost)


