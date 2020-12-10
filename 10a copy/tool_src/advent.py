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

def processStruct(struct):

    struct.sort()

    stepDist = [0,0,0,0,0]
    joltage = 0

    for adaptorOutput in struct:
        difference = adaptorOutput - joltage
        assert difference  < 4 and difference > 0
        joltage  = adaptorOutput
        stepDist[difference] = stepDist[difference]+1

    stepDist[3] = stepDist[3] +1
    joltage = joltage + 3

    return stepDist[1] * stepDist[3]

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    #print(struct)
    print( processStruct(struct) )

if __name__ == "__main__":

    mainTask()