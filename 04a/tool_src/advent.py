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

    
    validValues = []
    numberOfPassports = len(struct)
    print("Number of numberOfPassports %d" %(numberOfPassports))

    for passport in struct :
        lines = re.split('[\n :]',passport)
        print(lines)
        a = "byr" in lines
        b = "iyr" in lines
        c = "eyr" in lines
        d = "hgt" in lines
        e = "hcl" in lines
        f = "ecl" in lines
        g = "pid" in lines
        #"cid"
        if a and b and c and d and e and f and g :
            validValues.append(passport)

    print(len(validValues))


def mainTask():
    input_path = os.path.join(os.path.dirname(__file__),"input.txt")
    struct = processInputFile(input_path)
    processStruct(struct)

if __name__ == "__main__":

    mainTask()