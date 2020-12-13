import os
import re
import copy
import math

def processLineOfInputIntoStruct(line,struct):
    intstrs = line.split(",")
    for x in intstrs:
        if (x.strip() != "x"):
            struct.append(int(x.strip()))


def processInputFile(filePath):
    
    course = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,course)
        f.close()
    else :
        print("%s does not exist"%(filePath))

    return course

def nextBusLeavesIn(targetTime,base):
    fac = math.floor(targetTime / base)

    multA = fac * base
    if (multA < targetTime):
        multA = (fac+1) * base
        assert multA >= targetTime

    timeD =multA - targetTime 
    print("Bus ID %d leaves at %d - %d minutes after %d"%(base,multA,timeD,targetTime))
    return timeD

def processStruct(struct):

    target = struct[0]
    best = target
    bestID = -1
    for busId in struct[1:]:
        diff = nextBusLeavesIn(target,busId)
        assert diff != best
        if diff < best :
            bestID = busId
            best = diff

    # What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
    print("Best bus is %d with %d min wait"%(bestID,best))
    return bestID * best

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    print("answer %d"%(processStruct(struct)))
    

if __name__ == "__main__":

    mainTask()