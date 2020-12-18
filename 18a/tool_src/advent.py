import os
import re
import copy
import math

def sumWithoutBrackets(line):
    assert "(" not in line
    assert ")" not in line
    #9 * 8 + 13 * 3 + 5
    # left to right.

    vals = line.strip().replace("  "," ").split(" ")
    sum = int(vals[0])
    i = 1
    while ( i < len(vals) ):
        nexInt = int(vals[i+1])
        if (vals[i] =="*"):
            sum = sum * nexInt
        elif (vals[i] =="+"):
            sum = sum + nexInt
        i = i + 2
    return sum

def firstFirstPairOfBrackets(line):
    if ")" in line:
        firstClosePos =line.index(")")
        #backtract to find nearest "("
        for i in range(firstClosePos-1)[::-1]:
            if line[i] == "(":
                #print(line[i:firstClosePos+1])
                return (i,firstClosePos+1)
    return (-1,0)


def splitLine(line,a,b):
    #split line into 3 parts
    stringA = line[0:a]
    stringB = line[a:b]
    stringC = line[b:len(line)]
    return (stringA,stringB,stringC)

def replaceFirstStringWithinBrackets(line):
    newline = line
    firstSub = firstFirstPairOfBrackets(line)
    if firstSub != (-1,0):
        (strA,strB,strC) = splitLine(line,firstSub[0],firstSub[1])
        # strB should have no brackets in
        intVal = sumWithoutBrackets(strB[1:-1])
        #return (line[0:a-1],line[a:b],line[b:len(line)])
        midStr = str(intVal)
        firstStr = strA + midStr
        secondStr = firstStr + strC
        newline = secondStr
    return newline

def reduceStringToSingleValue(line):
    
    while "(" in line:
        print(line)
        line = replaceFirstStringWithinBrackets(line)
    
    sum = sumWithoutBrackets(line)
#    (a,b) = firstDeepestPairOfBrackets(line)
    return sum

def processLineOfInputIntoStruct(l,struct):
    struct.append(l)

def processInputFile(filePath):
   
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for l in f:
            processLineOfInputIntoStruct(l,struct)
        f.close()
    else :
        print("%s does not exist"%(filePath))
    
    return struct

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    sum = 0
    for l in struct:
        sum = sum + reduceStringToSingleValue(l)
    print(sum)

if __name__ == "__main__":

    mainTask()