import os
import re
import copy
import math

def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(36)[::-1])

def applyMaskBinary(maskBits,value):

    maskLen = len(maskBits)
    assert maskLen == 36
    valueBits = toBinary(value)
    outputValue = 0
    for i in range(36)[::-1]:
        if maskBits[i] == 'X':
            if valueBits[i] == '1':
                outputValue = outputValue = 2^i
        elif maskBits[i] == '1':
            outputValue = outputValue = 2^i
        else:
            assert maskBits[i] == '0'
    return outputValue


def processLineOfInputIntoStruct(line,struct):
    intstrs = line.split("=")

    if intstrs[0].strip() == "mask":
        # process bitmask into int
        maskValue = intstrs[1].strip()
        struct.append((-1,maskValue))
    else:
        #mem[54152] = 692939
        lbRemove =intstrs[0].replace("mem["," ")
        rbRemove =lbRemove.replace("]"," ")
        address = int(rbRemove.strip())
        value = int(intstrs[1])
        struct.append((address,value))

    return struct

def processInputFile(filePath):
    
    course = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,course)
        f.close()
    else :
        print("%s does not exist"%(filePath))

    return course

def processStruct(struct):

    memory = {}
    currentMask = ""
    for inst in struct:
        if inst[0] == -1:
            # change mask
            currentMask = inst[1]
        else:
            val = applyMaskBinary(currentMask,inst[1])
            memory[inst[0]] = val

    sum = 0
    for pairs in memory :
        sum = sum + memory[pairs]

    print("sum = %d"%(sum))
    return sum

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    print("answer %d"%(processStruct(struct)))
    

if __name__ == "__main__":

    mainTask()