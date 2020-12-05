import os
import re

def isCharacterN(stringValue,characterIndex,wantedChar):
    return stringValue[characterIndex] == wantedChar

def processLineOfInputIntoStruct(line,struct):
    struct.append(line.strip())

def processInputFile(filePath):
    
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x,struct)
    else :
        print("%s does not exist"%(filePath))
    return struct

def IsLorR(seat,index,valueForF,valueForB):
    if (isCharacterN(seat,index,"L")):
        return valueForF
    if (isCharacterN(seat,index,"R")):
        return valueForB
    
    print("Error with character %d in %s"%(index,seat))
    return 0


def IsForB(seat,index,valueForF,valueForB):
    if (isCharacterN(seat,index,"F")):
        return valueForF
    if (isCharacterN(seat,index,"B")):
        return valueForB
    
    print("Error with character %d in %s"%(index,seat))
    return 0

def processStruct(struct):

    validValues = []
    numberOfSeats = len(struct)
    print("Number of numberOfSeats %d" %(numberOfSeats))

    for seat in struct :
        seatRow = 0
        seatCol = 0
        # First char tells you if you are in 0-63 or 64-127
        seatRow = seatRow + IsForB(seat,0,0,64)
        seatRow = seatRow + IsForB(seat,1,0,32)
        seatRow = seatRow + IsForB(seat,2,0,16)
        seatRow = seatRow + IsForB(seat,3,0,8)
        seatRow = seatRow + IsForB(seat,4,0,4)
        seatRow = seatRow + IsForB(seat,5,0,2)
        seatRow = seatRow + IsForB(seat,6,0,1)

        seatCol = seatCol + IsLorR(seat,7,0,4)
        seatCol = seatCol + IsLorR(seat,8,0,2)
        seatCol = seatCol + IsLorR(seat,9,0,1)

        id = (seatRow * 8) + seatCol
        validValues.append(id)

    print(len(validValues))
    validValues.sort()
    print(validValues[-1])


def mainTask():
    input_path = os.path.join(os.path.dirname(__file__),"input.txt")
    struct = processInputFile(input_path)
    processStruct(struct)

# The first 7 characters will either be F or B; 
# these specify exactly one of the 128 rows on the plane (numbered 0 through 127)
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7)
# decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

#Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

if __name__ == "__main__":

    mainTask()