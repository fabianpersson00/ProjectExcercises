'''
**Closest pair problem** 
- 
The closest pair of points problem or closest pair problem is a problem of computational geometry;
Given *n* points in metric space, find a pair of points with the smallest distance between them.
'''
import math

'(x, y)'
test1Points2D = [(5, 97), (30, 83), (50, 94), (74, 84), (95, 96), (65, 60), (5, 50), (45, 51), (81, 49), (20, 19), (50, 5), (99, 7)]

def measureDistance(point1, point2):
    'Return the distance between these two points.'
    pointX = point1[0] - point2[0]
    pointY = point1[1] - point2[1]
    distance = (pointX**2 + pointY**2)**0.5
    return distance

def closestPair(listOfPoints):
    'Return the two points in the list with the shortest distance inbetween.'
    resultDict = {
        "primaryPoint": (),
        "secondaryPoint": (),
        "distance": math.inf
    }

    for index in range(len(listOfPoints)-1):
        primaryPoint = listOfPoints[index]
        while index < len(listOfPoints)-1:
            index += 1
            secondaryPoint = listOfPoints[index]
            distanceBetween = measureDistance(primaryPoint, secondaryPoint)
            if distanceBetween < resultDict['distance']:
                resultDict.update({"primaryPoint": primaryPoint, "secondaryPoint": secondaryPoint, "distance": distanceBetween})
    return resultDict

print(closestPair(test1Points2D))