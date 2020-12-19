import os
import re
import copy
import math


def mostLikely2SplitsFirst(remainingString):

    ps = range(1,len(remainingString))
    average = sum(ps) / len(ps)
    pairs = []
    for p in ps:
        pairs.append((p,abs(average-p)))

    pairs.sort(key=lambda x: x[1])
    sortedValues = []
    for p in pairs:
        sortedValues.append(p[0])
    return sortedValues


def testAllPossible2Splits(remainingString,ruleLeft,ruleRight,recursionControl,ruleStuct):
    foundMatch = False

    if len(remainingString) < 2: 
        return False

    rangeA = mostLikely2SplitsFirst(remainingString)

    for splitPosition in rangeA:#range(1,len(remainingString)):
        leftStr = remainingString[0:splitPosition]
        assert len(leftStr) > 0
        rightStr = remainingString[splitPosition:len(remainingString)]
        assert len(rightStr) > 0
        remade = leftStr+rightStr
        assert remade == remainingString
        canMatchLeft = canIMatchThisStringForThisRule(leftStr,ruleLeft,recursionControl,ruleStuct)
        if canMatchLeft:
            canMatchRight = canIMatchThisStringForThisRule(rightStr,ruleRight,recursionControl,ruleStuct)
            if (canMatchRight):
                return True
    return foundMatch

def testAllPossible3Splits(remainingString,ruleA,ruleB,ruleC,recursionControl,ruleStuct):
    foundMatch = False
    
    if len(remainingString) < 3: 
        return False

    for splitPositionA in range(1,len(remainingString)-2):
        aStr = remainingString[0:splitPositionA]
        for splitPositionB in range(splitPositionA+1,len(remainingString)):
            bStr = remainingString[splitPositionA:splitPositionB]
            cStr = remainingString[splitPositionB:len(remainingString)]
            assert len(aStr) > 0
            assert len(bStr) > 0
            assert len(cStr) > 0
            assert aStr+bStr+cStr == remainingString

            canMatchA = canIMatchThisStringForThisRule(aStr,ruleA,recursionControl,ruleStuct)
            if canMatchA:
                canMatchB = canIMatchThisStringForThisRule(bStr,ruleB,recursionControl,ruleStuct)
                if (canMatchB):
                    canMatchC = canIMatchThisStringForThisRule(cStr,ruleC,recursionControl,ruleStuct)
                    if (canMatchC):
                        return True
    return foundMatch



def canIMatchThisStringForThisRule(remainingString,ruleN,recursionControl,ruleStuct):
    assert ruleN in ruleStuct
    choices = ruleStuct[ruleN]
    # No rules match to empty
    
    foundMatch = False

     # If rule has one option
    if len(choices) == 1:
        parts = choices[0]
        # if option has one part
        if len(parts) == 1:
            # if part it terminal, return character
            if parts[0] == -1:
                foundMatch = "a" == remainingString
                #print("Match %s to rule %d is %s"%(remainingString,ruleN,foundMatch))
                return foundMatch
            elif parts[0] == -2:
                foundMatch = "b" == remainingString
                #print("Match %s to rule %d is %s"%(remainingString,ruleN,foundMatch))
                return foundMatch
    

    for choice in choices:
        parts = choice
        nParts = len(parts)
        assert nParts < 4
        assert nParts > 0
        # There is 1,2 or 3 parts to this choice
        if nParts == 1:
            if canIMatchThisStringForThisRule(remainingString,parts[0],recursionControl,ruleStuct):
                foundMatch = True
                break
        elif nParts == 2:
            if testAllPossible2Splits(remainingString,parts[0],parts[1],recursionControl,ruleStuct):
                foundMatch = True
                break
        elif nParts == 3:
            if testAllPossible3Splits(remainingString,parts[0],parts[1],parts[2],recursionControl,ruleStuct):
                foundMatch = True
                break

    #print("Match %s to rule %d is %s"%(remainingString,ruleN,foundMatch))

    return foundMatch



def testIsMessagesValid(ruleStruct,message):
    recursionControl = {}
    return canIMatchThisStringForThisRule(message,0,recursionControl,ruleStruct)

def testAllMessagesAndCountValid(ruleStruct,messages):
    validMessageCount = 0
    msgChecked = 0
    for message in messages:
        print("Checking message %d"%(msgChecked))
        msgChecked = msgChecked + 1
        if testIsMessagesValid(ruleStruct,message):
            validMessageCount = validMessageCount + 1
    return validMessageCount

def processLineOfInputIntoMessageStruct(line,messages):
    # ababbb
    messages.append(line.strip())

def processLineOfInputIntoRuleStruct(line,rules):
    # "1: 2 3 | 3 2"
    # A is -1
    # B is -2
    partsA = line.split(":")                # ["1","2 3 | 3 2"]
    assert len(partsA) == 2
    partsB = partsA[1].strip().split("|")   # '["2 3","3 2"]
    ruleInt = int(partsA[0].strip())
    for optionsStr in partsB:
        optionIntArray = []
        rulesInOption = optionsStr.strip().split(" ") # ["2","3"]
        for optionStr in rulesInOption:
            if optionStr.strip() == "\"a\"":
                optionIntArray.append(-1)
            elif optionStr.strip() == "\"b\"":
                optionIntArray.append(-2)
            else:
                optionIntArray.append(int(optionStr))
        if ruleInt not in rules:
            rules[ruleInt] = []
        rules[ruleInt].append(optionIntArray)


def processInputFile(filePath):
    
    rules = {}
    messages = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        loadingMessages = False
        for x in f:
            if x == "\n":
                loadingMessages = True
                continue
            if loadingMessages:
                processLineOfInputIntoMessageStruct(x,messages)
            else:
                processLineOfInputIntoRuleStruct(x,rules)
        f.close()
    else :
        print("%s does not exist"%(filePath))

    return (rules,messages)

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    rules, messages = processInputFile(input_path)
    count = testAllMessagesAndCountValid(rules,messages)
    print(count)

if __name__ == "__main__":

    mainTask()