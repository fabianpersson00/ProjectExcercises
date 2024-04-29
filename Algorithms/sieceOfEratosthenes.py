'''
**Sieve of Eratosthenes** 
- 
The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2. 
The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime.
'''
import math as ma

while True:
    try:
        upperLimit = int(input("Input the upper limit for the prime searching algorithm: "))
        break
    except ValueError:
        print("Wrong input, try again.")

'''
I'll use a list of booleans, but we assume once we iterate over it that the first bool if converted into integer would be a 2.
Then 3 for the second index and etc.
'''
def allPrimes(primeLimit):
    primeLimit -= 1
    primesBoolList = [True]
    primesBoolList = primesBoolList * primeLimit

    curr = 2
    while curr <= primeLimit:
        if primesBoolList[curr-2] == False:
            curr += 1
            continue
        else:
            steps = 2
            increment = curr * steps
            while increment <= primeLimit+1:
                primesBoolList[increment-2] = False
                steps +=1 
                increment = curr * steps
            curr += 1

    return boolListToPrimes(primesBoolList)

def boolListToPrimes(listOfBooleans):
    start = 2
    primesIntegerList = []
    for element in listOfBooleans:
        if element == True:
            primesIntegerList.append(start)
        start += 1
    return primesIntegerList

print(allPrimes(upperLimit))
