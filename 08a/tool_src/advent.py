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

    # Every line has one space
    instrAndValue = line.split(" ",2)
    assert len(instrAndValue) == 2

    accChange = int(instrAndValue[1])
    instr = instrAndValue[0].strip()
    struct.append((instr,accChange))

def processInputFile(filePath):
    
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,struct)
        f.close()
    else :
        print("%s does not exist"%(filePath))

    return struct



def processInstruction(instruction,state):
    programCounter,accumulator = (state)
    print("processInstruction %d (%s,%s)"%(programCounter,instruction[0],instruction[1]))
    
    if (instruction[0] == "acc"):
        accumulator = accumulator + instruction[1]
        programCounter = programCounter + 1
    if (instruction[0] == "jmp"):
        programCounter = programCounter + instruction[1]
    if (instruction[0] == "nop"):
        programCounter = programCounter + 1
    
    return (programCounter,accumulator)

def processStruct(struct):
    
    executedInstructions = set()
    accumulator = 0
    programCounter = 0
    state = (programCounter,accumulator)

    while True:
        nextInst = struct[state[0]]
        if state[0] in executedInstructions :
            print("instruction %d executed before"%(state[0]))
            print("accumulator value %d"%(state[1]))
            break
        else:
            executedInstructions.add(state[0])
            state = processInstruction(nextInst,state)
            

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    processStruct(struct)

if __name__ == "__main__":

    mainTask()

#