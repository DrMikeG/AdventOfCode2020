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



def mainTask():
    input_path = os.path.join(os.path.dirname(__file__),"input.txt")
    struct = processInputFile(input_path)
    processStruct(struct)

if __name__ == "__main__":

    mainTask()