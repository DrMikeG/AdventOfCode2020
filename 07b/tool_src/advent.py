import os
import re

def isCharacterN(stringValue,characterIndex,wantedChar):
    return stringValue[characterIndex] == wantedChar


def splitBagContain(wholeLine):
    #'light indigo bags contain 5 mirrored chartreuse bags.'
    # split into rule title and rule
    newString = wholeLine.replace("bags contain",",")
    newStringParts = newString.split(",")
    return newStringParts

def parseRuleTitle(ruleTitleString):
    #'mirrored orange '
    stringList = ruleTitleString.strip().split(" ",2)
    assert len(stringList) == 2
    ruleTitleTuple = (stringList[0].strip(),stringList[1].strip())
    return ruleTitleTuple

def parseContentRule(contentRuleDirtyString):
    #' 3 vibrant gray bags'
    #' 1 pale teal bag.\n'
    #' no other bags.'
    # remove bag of bags and anything after

    if "no other bags" in contentRuleDirtyString:
        return (0,"","")

    workingString = str()
    assert contentRuleDirtyString.find("bag") > -1
    workingString = contentRuleDirtyString[0:contentRuleDirtyString.find("bag")].strip()
    # '3 vibrant gray'
    # '1 pale teal'
    stringList = workingString.split(" ",3)
    assert len(stringList) == 3
    ruleTuple = (int(stringList[0]),stringList[1].strip(),stringList[2].strip())
    return ruleTuple

def processLineOfInputIntoStruct(line,struct):
    # split at 'bags contain' (each line should contain this)
    # split comma separated list ending with . (each line should contain this)
    # remove bag or bags
    # start with number
    # colour description contains exactly 1 space
    # map from colour description tuple array (1, col desc),(1, col desc),(1, col desc)
    newStringParts = splitBagContain(line)
    ruleTitle = parseRuleTitle(newStringParts[0])
    rules = list(map(parseContentRule,newStringParts[1:]))
    assert len(rules) > 0
    assert ruleTitle not in struct, "Duplicate key: %s,%s" %(ruleTitle[0],ruleTitle[1])
    struct[ruleTitle] = rules

def processInputFile(filePath):
    
    struct = {}
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,struct)
        f.close()
    else :
        print("%s does not exist"%(filePath))

    return struct



def followPathLookingFor(struct,stack,targetBag,bagCount):
    
    #is the stack empty?
    if (len(stack) == 0):
        return False
    
    #is the final thing on the stack targetBag?
    if (stack[-1] == targetBag):
        return True

    # remove the final thing from stack
    expanding = stack.pop(-1)
    bagCount = bagCount + 1
    # expanding is rule (1,'a','b')
    
    if ( expanding not in struct):
        print (expanding)
        assert expanding in struct, "key: %s not in rules" %(list(expanding))

    rules = struct[expanding]
    for rule in rules:
        assert len(rule) == 3, "Rules does not have three parts: %s" %(rule)
        ruleN = rule[0]
        ruleKey = (rule[1],rule[2])
        for _ in range(ruleN):
            stack.append(ruleKey)
            #print("adding %s" %(list(ruleKey)))

    print(stack)
    return followPathLookingFor(struct,stack,targetBag,bagCount)


def processStruct(struct):
    # You have a shiny gold bag.
    # If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? 
    # (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

    bagCount = 0
    startingBag = ('shiny','gold')
    stack = []
    stack.append(startingBag)
    followPathLookingFor(struct,stack,('shiny','gold'),bagCount)

    print(bagCount)

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"requirements.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    processStruct(struct)

if __name__ == "__main__":

    mainTask()

#