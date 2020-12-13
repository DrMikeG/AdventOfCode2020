import os
import re
import copy
import math

def processLineOfInputIntoStruct(line,struct):
    intstrs = line.split(",")
    xCount = 0
    for x in intstrs:
        if (x.strip() != "x"):
            struct.append((xCount,int(x.strip())))
            xCount = 0
        else:
            xCount = xCount+1


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

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))


def isBusTime(targetTime,base):
    div = targetTime / base
    return (div == math.floor(div))

def processStruct(struct):

    # each entry is offset,value
    
    listMin = struct[0][1]
    
    startAt = listMin * math.floor(100000090057500 / listMin)
    while True:
        timeWorksForAllBusses = True

        for offsetBusIDPair in struct:
            busId = offsetBusIDPair[1]
            time = startAt + offsetBusIDPair[0]
            if not isBusTime(time,busId):
                timeWorksForAllBusses = False
                break
        
        if (timeWorksForAllBusses):
            print("Answer timestamp is %d"%(startAt))

        startAt = startAt + listMin

        if (startAt % 100000000000 == 0):
            print(startAt)
    return startAt

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    print("answer %d"%(processStruct(struct)))
    

if __name__ == "__main__":

    mainTask()