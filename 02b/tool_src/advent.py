import os


def isCharacterN(stringValue,characterIndex,wantedChar):
    return stringValue[characterIndex-1] == wantedChar

def processLineOfInputIntoStruct(line,struct):
    rulePassword = line.split(":",2)
    ruleLetterMinMax = rulePassword[0].split(" ",2)
    ruleMinMax = ruleLetterMinMax[0].split("-",2)
    #struct.append(ruleMinMax)
    struct.append((ruleLetterMinMax[1].strip(),int(ruleMinMax[0].strip()),int(ruleMinMax[1].strip()),rulePassword[1].strip()))

def processInputFile(filePath):
    
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,struct)
    return struct

def processStruct(struct):
    validValues = []
    
    for value in struct:
        wantedChar = value[0]
        passwordCandidate = value[3]
        posAIsValid = isCharacterN(passwordCandidate,value[1],wantedChar)
        posBIsValid = isCharacterN(passwordCandidate,value[2],wantedChar)

        if (posAIsValid != posBIsValid) :
            validValues.append(passwordCandidate)
    print(validValues)
    print(len(validValues))

def mainTask():

    input_path = "C:\\Users\\gibbens\\Documents\\Arduino\\AdventOfCode2020\\02a\\tool_src\\input.txt"
    struct = processInputFile(input_path)
    processStruct(struct)
    


if __name__ == "__main__":

    mainTask()