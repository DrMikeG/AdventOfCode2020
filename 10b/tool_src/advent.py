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

    struct.sort()
    return struct

def structGetNextOptions(struct,joltage):
    couldUseNext = []
    for adaptorOutput in struct:
        difference = adaptorOutput - joltage
        if (difference >0 and difference < 4):
            couldUseNext.append(adaptorOutput)
        if (difference >= 4):
            break
    return couldUseNext

def followAndCountPaths(struct,cache,joltageIn,highest):

    if (joltageIn in cache):
        return cache[joltageIn]

    #print(joltageIn)
    if (joltageIn == highest):
        return 1

    branches = structGetNextOptions(struct,joltageIn)

    sum = 0
    for branch in branches:
        sum = sum + followAndCountPaths(struct,cache,branch,highest)
    
    cache[joltageIn] = sum
    return sum

def processStruct(struct):

    struct.sort()

    joltage = 0

    cache = dict()

    paths = followAndCountPaths(struct,cache,joltage,struct[-1])

    return paths

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    #print(struct)
    print( processStruct(struct) )
    # 5289227976704
if __name__ == "__main__":

    mainTask()