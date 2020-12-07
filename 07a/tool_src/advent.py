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

def processStruct(struct):

    sum = 0
    validValues = []
    numberOfPassports = len(struct)
    print("Number of numberOfPassports %d" %(numberOfPassports))

    for passport in struct :
        lines = re.split('[\n :]',passport)
        # which chars are in all lines?
        masterSet = set()
        first = True
        for line in lines:
            workingSet = set()
            for c in line:
                workingSet.add(c)
            print("Next answers:%s"%sorted(workingSet))
            if (len(workingSet) == 0):
                print("skipping empty line")
                continue
            
            if (first):
                first = False
                masterSet.update(workingSet)
                print("Master List: %s"%sorted(masterSet))
            else:
                print("Removing:    %s"%sorted(masterSet.difference(workingSet)))
                masterSet = masterSet.intersection(workingSet)
                print("Master List: %s"%sorted(masterSet))
        sum = sum + len(masterSet)
        print("Everyone in group answered yes to: %s\n"%sorted(masterSet))
        validValues.append(masterSet)
        
    #print(validValues)
    print(sum)

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"requirements.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    processStruct(struct)

if __name__ == "__main__":

    mainTask()