import os
import re
import copy
import math

def rowIndexAfter(struct,lineContains):
    for i in range(len(struct)):
        if lineContains in struct[i] :
            return i
    assert False

def parseTicketFromRowString(rowStr):
    intStrs = rowStr.split(",")
    ints = []
    for intStr in intStrs:
        ints.append(int(intStr))
    return ints

def parseFieldRuleFromRow(struct,rowIndex):
    #departure location: 37-594 or 615-952
    line = struct[rowIndex]
    nameAndRules = line.split(":")
    #departure location:
    name = nameAndRules[0].strip()
    #37-594 or 615-952
    ruleParts = nameAndRules[1].replace(" or "," ").strip().split(" ")
    assert len(ruleParts) == 2
    minA,maxA = ruleParts[0].split("-")
    minB,maxB = ruleParts[1].split("-")
    return (name,int(minA),int(maxA),int(minB),int(maxB))


def isNumberValidForRule(rule,number):
    if number >= rule[1] and number <= rule[2]:
        return True
    if number >= rule[3] and number <= rule[4]:
        return True
    return False

def isFieldValueValidForAnyRule(rules,number):
    isValid = False
    for rule in rules:
        if isNumberValidForRule(rule,number):
            isValid = True
            break
    return isValid

def findTicketValuesThatAreNotValid(rules,ticketValues):
    inValidValues = []
    for value in ticketValues:
        if not isFieldValueValidForAnyRule(rules,value):
            inValidValues.append(value)
    return inValidValues

def processLineOfInputIntoStruct(line,struct):
    # remove blank lines
    if (len(line.strip()) > 0):
        struct.append(line.strip())


def parseInputFile(struct):
    # make rules
    rules = []
    rulesEnd = rowIndexAfter(struct,"your ticket")
    for i in range(rulesEnd):
        rule = parseFieldRuleFromRow(struct,i)
        rules.append(rule)
    # make myTicket
    myTicket = parseTicketFromRowString(struct[rulesEnd+1])
    # make otherTickets
    otherIndex = rowIndexAfter(struct,"nearby tickets")+1
    otherTickets = []
    for i in range(otherIndex,len(struct)):
        otherTickets.append( parseTicketFromRowString(struct[i]) )

    return (rules, myTicket, otherTickets)


def sumIntsInArray(ints):
    sum = 0
    for i in ints:
        sum = sum + i
    return sum

def sumAllBadTicketValues(rules, myTicket, otherTickets):
    sum = 0
    for ticket in otherTickets:
        badInts = findTicketValuesThatAreNotValid(rules,ticket)
        sum = sum + sumIntsInArray(badInts)
    return sum


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
def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    allLines = processInputFile(input_path)
    rules, myTicket, otherTickets = parseInputFile(allLines)
    sum = sumAllBadTicketValues(rules, myTicket, otherTickets)
    print(sum)

if __name__ == "__main__":

    mainTask()