import os
import re

def processLineOfInputIntoStruct(line,struct):

    # Every line has one space
    instrAndValue = line.split(" ",2)
    assert len(instrAndValue) == 2

    accChange = int(instrAndValue[1])
    instr = instrAndValue[0].strip()
    assert len(instr) == 3
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

def indicesOfJmps(struct):
    jmps = []
    assert len(struct) 
    for i in range( len(struct) ):
        if (struct[i][0] == "jmp"):
            jmps.append(i)

    assert len(jmps) == 225

    return jmps

def indicesOfNops(struct):
    jmps = []
    for i in range( len(struct) + 1 ):
        if (struct[i][0] == "nop"):
            jmps.append(i)

    assert len(jmps) == 56

    return jmps



def processInstruction(instruction,state):

    programCounter,accumulator = (state)
    #print("processInstruction %d (%s,%s)"%(programCounter,instruction[0],instruction[1]))
    instStr,intValue = (instruction)
    
    if (instStr == "acc"):
        accumulator = accumulator + intValue
        programCounter = programCounter + 1
    elif (instStr == "jmp"):
        programCounter = programCounter + intValue
    elif (instStr == "nop"):
        programCounter = programCounter + 1
    else :
        assert False == True

    return (programCounter,accumulator)


def changeOperation(struct,n):
    assert n < len(struct)
    assert n > -1
    assert struct[n][0] == "jmp" or struct[n][0] == "nop"
    if struct[n][0] == "jmp":
        newOp = ("nop",struct[n][1])
        print("\nChanging instruction %d from %s,%s to %s,%s"%(n,struct[n][0],struct[n][1],newOp[0],newOp[1]))
        struct[n] = newOp

    elif struct[n][0] == "nop":
        newOp = ("jmp",struct[n][1])
        print("\nChanging instruction %d from %s,%s to %s,%s"%(n,struct[n][0],struct[n][1],newOp[0],newOp[1]))
        struct[n] = newOp

def processStruct(struct):

    # The program is supposed to terminate by attempting to execute an instruction 
    # immediately after the last instruction in the file. By changing exactly one jmp or nop,
    # you can repair the boot code and make it terminate correctly.

    executedInstructions = set()
    accumulator = 0
    programCounter = 0
    state = (programCounter,accumulator)
    finalInstruction = len(struct)

    assert finalInstruction == 611

    while True:
        if state[0] in executedInstructions :
            print("Program would loop forever")
            print("instruction %d executed before"%(state[0]))
            print("accumulator value %d"%(state[1]))
            return False # Would have looped forever
        else:
            executedInstructions.add(state[0])
            if (state[0] == finalInstruction):
                print("Program reached final instruction")
                # Cannot process final instruction as it is not known...
                #state = processInstruction(nextInst,state)
                print("accumulator value %d"%(state[1]))
                return True
            elif (state[0] < 0):
                print("last jump was to before start of program block")
                return False
            elif (state[0] > finalInstruction):
                print("last jump was to after end of program block")
                return False
            else:
                nextInst = struct[state[0]]
                state = processInstruction(nextInst,state)
            
    return False

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()

    struct = processInputFile(input_path)

    #processStruct(struct)

    jmps = indicesOfJmps(struct)
    nops = indicesOfNops(struct)

    for jump in jmps :
        newStruct = processInputFile(input_path)
        changeOperation(newStruct,jump)
        assert newStruct != struct
        if processStruct(newStruct) : 
            break
    
    for nop in nops :
        newStruct = processInputFile(input_path)
        changeOperation(newStruct,nop)
        assert newStruct != struct
        if processStruct(newStruct) : 
            break

if __name__ == "__main__":

    mainTask()