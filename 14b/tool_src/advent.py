import os
import re
import copy
import math

def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(36)[::-1])

def toInt(binStr32):
    return  int(binStr32,2)

def expandFirstXAndRecurse(inputString,output):
    if not 'X' in inputString:
        output.append(inputString)
        return
    else:
        expandFirstXAndRecurse(inputString.replace("X","0",1),output)
        expandFirstXAndRecurse(inputString.replace("X","1",1),output)

def getAddressForFloating(maskBits,baseAddress):
    # Apply bitmask to address
    #If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    #If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.

    baseAsString = toBinary(baseAddress)
    newString = ""
    for i in range(36):
        if (maskBits[i] == '1'):
            newString += '1'
        elif (maskBits[i] == 'X'):
            newString += 'X'
        else:
            newString += baseAsString[i]

    # Expand all floating
    outputAddressAsInt = []
    outputAddress = []
    expandFirstXAndRecurse(newString,outputAddress)
    for add in outputAddress:
        outputAddressAsInt.append(toInt(add))

    return outputAddressAsInt


def writeToMemory(maskBits,instruction,memory):

    address, value = instruction

    #Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

    addresses = getAddressForFloating(maskBits,address)
    for add in addresses:
        memory[add] = value



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
            writeToMemory(currentMask,inst,memory)

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