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

def removeAllBadTickets(rules, myTicket, otherTickets):
    goodTickets = []
    for ticket in otherTickets:
        badInts = findTicketValuesThatAreNotValid(rules,ticket)
        if len(badInts) == 0:
            goodTickets.append(ticket)
    return goodTickets


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

def whichRuleIsValidForFieldNOnAllGoodTickets(rules,goodTickets,n):
    validRules = []
    for rule in rules:
        canHaveThisRule = True
        for ticket in goodTickets:
            if not isNumberValidForRule(rule,ticket[n]) :
                canHaveThisRule = False
                break
        # we have found a ticket the isn't value for this rule
        if canHaveThisRule:
            validRules.append(rule[0])
    print("Field %d could be %s"%(n,list(validRules)))
    return validRules

def whichRulesCouldBeWhichFields(rules,goodTickets):
    nRules = len(rules)
    nFields = len(goodTickets[0])
    print("There are %d fields and %d rules"%(nFields,nRules))
    possibles = []
    for i in range(nFields):
        possibles.append(whichRuleIsValidForFieldNOnAllGoodTickets(rules,goodTickets,i))
    return possibles

def eliminate(rules, myTicket, otherTickets):
    goodTickets = removeAllBadTickets(rules, myTicket, otherTickets)
    goodTickets.append(myTicket)
    possibles = whichRulesCouldBeWhichFields(rules,goodTickets)
    return possibles

def processOfElimination(possibles):
    # What are all the possibles that have only one value
    # are they unique?
    # they should be removed from all other possibles
    onlyOption = []
    for possible in possibles:
        if len(possible) == 1 :
            onlyOption.append(possible[0])
    assert len(onlyOption) == len(set(onlyOption))

    goAgain = False
    reducedPossibles = []
    for possible in possibles:
        if (len(possible) > 1):
            validOptions = []
            for option in possible:
                if option not in onlyOption:
                    validOptions.append(option)
            # replace possible with validOptions (having removed ones not allowed)            
            reducedPossibles.append(validOptions)
            if len(validOptions) > 1:
                goAgain = True
        else:
            # possible set of class names can remain unchanged (length == 1)
            reducedPossibles.append(possible)

    if goAgain:
        return processOfElimination(reducedPossibles)

    print("Fields must be in order ",reducedPossibles)
    return reducedPossibles

def mainTask():
    input_path = getInputPath()
    allLines = processInputFile(input_path)
    rules, myTicket, otherTickets = parseInputFile(allLines)
    possibles = eliminate(rules, myTicket, otherTickets)
    correctFieldOrder = processOfElimination(possibles)

    product = 1
    for i in range(len(correctFieldOrder)):
        if (correctFieldOrder[i][0].startswith("departure")):
            print("%i : %s"%(i,correctFieldOrder[i][0]))
            product = product * myTicket[i]

    print (product)

if __name__ == "__main__":

    mainTask()