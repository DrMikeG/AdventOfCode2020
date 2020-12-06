import os
import re

def isCharacterN(stringValue,characterIndex,wantedChar):
    return stringValue[characterIndex] == wantedChar

def processLineOfInputIntoStruct(line,struct):
    struct.append(line)

def processInputFile(filePath):
    
    struct = []
    if os.path.exists(filePath):
        with open(filePath) as f:
            lines = f.read()
        struct = lines.split("\n\n")
    else :
        print("%s does not exist"%(filePath))
    return struct

def processStruct(struct):

    sum = 0
    validValues = []
    numberOfPassports = len(struct)
    print("Number of numberOfPassports %d" %(numberOfPassports))

    for passport in struct :
        uniqueChars = set()
        lines = re.split('[\n :]',passport)
        for line in lines:
            for c in line:
                uniqueChars.add(c)
        validValues.append(uniqueChars)
        sum = sum + len(uniqueChars)
    print(validValues)
    print(sum)



def mainTask():
    input_path = os.path.join(os.path.dirname(__file__),"input.txt")
    struct = processInputFile(input_path)
    processStruct(struct)

if __name__ == "__main__":

    mainTask()