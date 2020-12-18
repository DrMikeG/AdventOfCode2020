import os
import re
import copy
import math

def sumWithoutBrackets(line):
    assert "(" not in line
    assert ")" not in line
    #9 * 8 + 13 * 3 + 5
    # left to right.

    # we new need to recursivly split by *

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



def insertBracketsForAdditionAt(line,n):
    assert line[n] == "+"
    # Figure out the term to the left of the +?
    # Figure out the term to the right of the +?
    # going left
    # either a single number or )
    # if you pass an ), you must continue to it's corresponding (
    # inject left (
    # going right
    # either a single number or (
    # if you pass an (, you must continue to it's corresponding )
    # inject right )

    leftInjectionPoint = 0
    leftStart = n-1
    while line[leftStart] == " ":
        leftStart = leftStart-1
    # first character that is not a space
    # if first character is ) then walk back to match bracket
    lOpen = 0
    lClose = 1
    if line[leftStart] == ")":
        for lpos in reversed(range(leftStart)):
            if line[lpos] == "(":
                lOpen = lOpen + 1
            if line[lpos] == ")":
                lClose = lClose + 1
            if lClose == lOpen:
                leftInjectionPoint = lpos
                break
    else: # line[leftStart] is digit
        for lpos in reversed(range(leftStart+1)):
            if line[lpos] == " ":
                leftInjectionPoint = lpos
                break

    rightInjectionPoint = len(line)
    rightStart = n+1
    while line[rightStart] == " ":
        rightStart = rightStart+1
    # first character that is not a space
    # if first character is ( then walk back to match bracket
    rOpen = 1
    rClose = 0
    if line[rightStart] == "(":
        for rpos in range(rightStart+1,len(line)-1):
            if line[rpos] == "(":
                rOpen = rOpen + 1
            if line[rpos] == ")":
                rClose = rClose + 1
            if rClose == rOpen:
                rightInjectionPoint = rpos
                break
    else: # line[rightStart] is digit
        for rpos in range(rightStart,len(line)-1):
            if line[rpos] == " ":
                rightInjectionPoint = rpos
                break

    stringA = line[0:leftInjectionPoint]
    stringB = line[leftInjectionPoint:rightInjectionPoint]
    stringC = line[rightInjectionPoint:len(line)]
    stringD  = (stringA + " ( " + stringB + " ) " + stringC).replace("  "," ")

    return stringD


def positionsOfPlus(l):
    positions = []
    for i in range(len(l)):
        if l[i] == "+":
            positions.append(i)
    return positions

def insertBracketsForAllAdditions(l):
    # count the +
    # for each + in turn, from the left
    nPositions= len(positionsOfPlus(l))
    for n in range(nPositions):
        print(l)
        pos = positionsOfPlus(l)[n]
        l = insertBracketsForAdditionAt(l,pos)

    return l

def processLineOfInputIntoStruct(l,struct):
    struct.append(insertBracketsForAllAdditions(l))

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