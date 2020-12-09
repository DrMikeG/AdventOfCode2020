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

def processStruct(struct,preampleLength):

    stopAt = len(struct)

    for indexUnderTest in getRange(preampleLength,stopAt) :
        numbers = getNPreviousNumbers(struct,indexUnderTest,preampleLength)
        toTest = struct[indexUnderTest]
        if not rangeHasPairTheSumToN(numbers,toTest):
            print("%d is not sum of number in previous 25"%(toTest))
            print(list(numbers))
            return toTest

    return -1

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    preampleLength = 25

    found = processStruct(struct,preampleLength)

if __name__ == "__main__":

    mainTask()