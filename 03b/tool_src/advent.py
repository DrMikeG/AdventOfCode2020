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

def altElement(a):
    return a[::2]

def processStruct(structB):

    struct = altElement(structB)
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
        posFromLeft = posFromLeft + 1
    
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

    #input_path = "C:\\Users\\gibbens\\Documents\\Arduino\\AdventOfCode2020\\03a\\tool_src\\input.txt"
    #struct = processInputFile(input_path)
    #processStruct(struct)
    
# right 1, down 1 = 93
# right 3, down 1 = 164
# right 5, down 1 = 82
# right 7, down 1 = 91
# Right 1, down 2 = 44
    print (93*164*82*91*44)

if __name__ == "__main__":

    mainTask()