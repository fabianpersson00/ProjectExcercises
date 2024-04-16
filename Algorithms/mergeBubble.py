'''
**Sorting** - Implement two types of sorting algorithms: Merge sort and bubble sort.
'''
import math
import time

testList1 = [3, 8, 4, 1, 1, 5, 7, 3]
testList2 = [3, 8, 4, 1, 5, 1, 5, 7, 3]
testList3 = [10, 9 ,8, 7, 6, 5, 4, 3, 2, 1, 0]

def MergeSort(listOfElements):
    if len(listOfElements) == 1:
        return listOfElements
    
    middlePoint = math.floor(len(listOfElements)/2)
    leftList = MergeSort(listOfElements[:middlePoint])
    rightList = MergeSort(listOfElements[middlePoint:])

    return MergeElements(leftList, rightList)

def MergeElements(leftList, rightList):
    '''
    for each elements in both lists
    compare elements in index 0 to eachother, then pop for that list, and add to a new list
    once all elements have been checked, returned the new list
    '''
    mergedList = []
    'Compare the two elements, smallest goes to back first, then larger elements gets appended.'
    while len(leftList) > 0 and len(rightList) > 0:
        if leftList[0] < rightList[0]:
            mergedList.append(leftList[0])
            leftList.pop(0)
        else:
            mergedList.append(rightList[0])
            rightList.pop(0)
    
    'Now either leftList or rightList is empty, so we append the rest to the end of new list'
    while len(leftList) > 0:
        mergedList.append(leftList[0])
        leftList.pop(0)

    while len(rightList) > 0:
        mergedList.append(rightList[0])
        rightList.pop(0)

    return mergedList

def BubbleSort(listOfElements):
    sorted = False
    while sorted == False:
        sorted = True
        for index in range(len(listOfElements)-1):
            if listOfElements[index] > listOfElements[index+1]:
                temp = listOfElements[index+1]
                listOfElements[index+1] = listOfElements[index]
                listOfElements[index] = temp
                sorted = False
            
    return listOfElements

print("Merged sort test 1: ", MergeSort(testList1))
print("Merged sort test 2: ", MergeSort(testList2))
print("Merged sort test 3: ", MergeSort(testList3))
print("Bubble sort test 1: ", BubbleSort(testList1))
print("Bubble sort test 2: ", BubbleSort(testList2))
print("Bubble sort test 3: ", BubbleSort(testList3))