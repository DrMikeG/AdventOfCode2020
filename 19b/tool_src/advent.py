import os
import re
import copy
import math

def everyAWithEveryB(aS,bS):
    ret = []
    for a in aS:
        for b in bS:
            ret.append(a+b)
    return ret

def followAndCombinePartsAndB(ruleStuct,ruleA,ruleB,cutOff):
    aS = followEveryPath(ruleStuct,ruleA,cutOff) # array of possible values for ruleA
    bS = followEveryPath(ruleStuct,ruleB,cutOff) # array of possible values for ruleB
    return everyAWithEveryB(aS,bS) # all possible combinations of AB

def followAndCombinePartsAndBAndC(ruleStuct,ruleA,ruleB,ruleC,cutOff):
    aS = followEveryPath(ruleStuct,ruleA,cutOff) # array of possible values for ruleA
    bS = followEveryPath(ruleStuct,ruleB,cutOff) # array of possible values for ruleB
    cS = followEveryPath(ruleStuct,ruleC,cutOff) # array of possible values for rulec
    t = everyAWithEveryB(aS,bS)
    return everyAWithEveryB(t,cS) # all possible combinations of ABC



def followEveryPath(ruleStuct,rule,cutOff):

  

    assert rule in ruleStuct
    choices = ruleStuct[rule]
    
    # If rule has one option
    if len(choices) == 1:
        parts = choices[0]
        # if option has one part
        if len(parts) == 1:
            # if part it terminal, return character
            if parts[0] == -1:
                return ["a"]
            elif parts[0] == -2:
                return ["b"]

    # Options from this point one are:
    # A or B
    possibilities = []


    # 8: 42 | 42 8
    # If we reach rule 8,
    # if rule == 8 and cutOff > 3, do not expand second choice of rule 8 (only first)
    # if rule == 8 and cutOff < 3, cutOff = cutOff+1

    # 11: 42 31 | 42 11 31
    # If we reach rule 10,
    # if rule == 11 and cutOff > 3, do not expand second choice of rule 11 (only first)
    # if rule == 11 and cutOff < 3, cutOff = cutOff+1
    
    if rule == 8:
        if cutOff > 1:
            t = followEveryPath(ruleStuct,42,cutOff+1)
            possibilities.extend(t)
            return possibilities
        else:
            t = followAndCombinePartsAndB(ruleStuct,42,8,cutOff+1)
            possibilities.extend(t)
            return possibilities
    
    if rule == 11:
        if cutOff > 1:
            t = followAndCombinePartsAndB(ruleStuct,42,31,cutOff+1)
            possibilities.extend(t)
            return possibilities
        else :
            t = followAndCombinePartsAndBAndC(ruleStuct,42,11,31,cutOff+1)
            possibilities.extend(t)
            return possibilities

    for choice in choices:

        #for choice in choices:
        # only consider choice 0
        parts = choice
        nParts = len(parts)
        assert nParts < 4
        assert nParts > 0
        #We need to expand and concaternate all the parts
        if nParts == 1:
            t = followEveryPath(ruleStuct,parts[0],cutOff) # []
            possibilities.extend(t)
        elif nParts == 2:
            t = followAndCombinePartsAndB(ruleStuct,parts[0],parts[1],cutOff)
            possibilities.extend(t)
        elif nParts == 3:
            t = followAndCombinePartsAndBAndC(ruleStuct,parts[0],parts[1],parts[2],cutOff)
            possibilities.extend(t)

    return possibilities

def testAllMessagesAndCountValid(ruleStruct,messages):
    validMessageCount = 0
    print("Calculating valid message strings....")
    allValidMessages = followEveryPath(ruleStruct,0,0)
    print("Testing valid messages from intput....")
    for message in messages:
        if message in allValidMessages:
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