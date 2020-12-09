import os
import re

def processLineOfInputIntoStruct(line,struct):

    # Every line has one space
    lineAsNumber = int(line)
    assert lineAsNumber > 0
    struct.append(lineAsNumber)

def processInputFile(filePath):
    
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,struct)
        f.close()
    else :
        print("%s does not exist"%(filePath))

    return struct

def getNPreviousNumbers(struct,index,n):
    assert index >= n
    assert index < len(struct)
    start = index-n
    stop = index
    return struct[start:stop]


def rangeHasPairTheSumToN(numbers,target):
    for a in numbers :
        if a <= target :
            if (target - a ) != a:
                b = (target - a )
                if (b in numbers ):
                    return True
    return False

def getRange(preampleLength,stopAt):
    return range(preampleLength,stopAt)

def processStruct(struct,targetValue):

    
    # you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
    # To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

    stopAt = len(struct)

    for startingPos in range(0,stopAt):
        currentSum = struct[startingPos]
        assert currentSum < targetValue
        i = startingPos + 1
        smallest = currentSum
        largest = currentSum
        while currentSum < targetValue:
            
            if i > stopAt:
                break
            
            nextNumberToAdd = struct[i]
            
            if nextNumberToAdd < smallest:
                smallest = nextNumberToAdd

            if nextNumberToAdd > largest:
                largest = nextNumberToAdd

            currentSum = currentSum + nextNumberToAdd
            i = i + 1
            
            if currentSum == targetValue:
                print("Found target %d with sum of %d"%(targetValue,(smallest + largest)))
                return smallest + largest
            
            if currentSum > targetValue:
                break
    
    return -1

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    
    targetValue = 248131121
    found = processStruct(struct,targetValue)

if __name__ == "__main__":

    mainTask()