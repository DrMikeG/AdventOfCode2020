import os


def isCharacterN(stringValue,characterIndex,wantedChar):
    return stringValue[characterIndex] == wantedChar

def processLineOfInputIntoStruct(line,struct):
    struct.append(line)

def processInputFile(filePath):
    
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,struct)
    return struct

def processStruct(struct):
    ##validValues = []
    width = len(struct[0])
    print("Number of characters in first line is %d" %(width)) # 32 spaces across Toboggan slope
    numberOfLines = len(struct)
    print("Number of lines down the hill %d" %(numberOfLines))


    trees = 0
    notTrees = 0
    posFromLeft = 0
    for line in struct :
        posFromLeft = posFromLeft % 31
        print(line.strip())
        henryString = list("                                 ")
        
        if isCharacterN(line,posFromLeft,'.') :
            notTrees = notTrees + 1
            henryString[posFromLeft] = 'O'
        else :
            trees = trees + 1
            henryString[posFromLeft] = 'X'
        print("".join(henryString))
        posFromLeft = posFromLeft + 3
    
    print(trees)

    """
    for value in struct:
        wantedChar = value[0]
        passwordCandidate = value[3]
        posAIsValid = isCharacterN(passwordCandidate,value[1],wantedChar)
        posBIsValid = isCharacterN(passwordCandidate,value[2],wantedChar)

        if (posAIsValid != posBIsValid) :
            validValues.append(passwordCandidate)
    print(validValues)
    print(len(validValues))
    """
def mainTask():

    input_path = "C:\\Users\\gibbens\\Documents\\Arduino\\AdventOfCode2020\\03a\\tool_src\\input.txt"
    struct = processInputFile(input_path)
    processStruct(struct)
    
    


if __name__ == "__main__":
# > 115
    mainTask()