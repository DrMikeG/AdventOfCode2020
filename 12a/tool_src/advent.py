import os
import re
import copy
import math

def processLineOfInputIntoStruct(line,struct):

    #W3     S4     E4     L90     W3    S3    E4    N2    F28    S2
    lineS = line.strip()
    inst = lineS[0]
    angleOrDistance =int(lineS[1:])
    struct.append((inst,angleOrDistance))


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

def changeHeading(heading,angleDelta):
    origHeading = heading
    assert(angleDelta < 360)
    assert(angleDelta > -360)

    heading = heading + angleDelta
    if (heading > 360):
        heading = heading - 360

    if (heading < -360):
        heading = heading + 360

    print("Heading changed from %d to %d (%d)"%(origHeading,heading,angleDelta))
    return heading

def moveInHeading(heading,distance,position):
    (xPos,yPos) = position
    print("Move foward %d on heading %d"%(distance,heading))
    # x component of heading * distance
    xComp = math.sin(math.radians(heading))
    xDelta = round(xComp * distance)
    print("Change in X is %d for giving %d"%(xComp,xDelta))
    xPos = xPos + xDelta
    # y component of heading * distance
    yComp = math.cos(math.radians(heading))
    yDelta = round(yComp * distance)
    print("Change in Y is %d for giving %d"%(yComp,yDelta))
    yPos = yPos + yDelta
    return (xPos,yPos)

def followCourse(course):
    #Ship is facing East
    heading =90
    xPos = 0
    yPos = 0

    for (inst,value) in course:
        print ("Moving %s by %d"%(inst,value))
        if (inst == 'N'):
            #Action N means to move north by the given value.
            yPos += value
        if (inst == 'S'):
            #Action S means to move south by the given value.
            yPos -= value
        if (inst == 'E'):
            #Action E means to move east by the given value.
            xPos += value
        if (inst == 'W'):
            #Action W means to move west by the given value.
            xPos -= value

        if (inst == 'L'):
            #Action L means to turn left the given number of degrees.
            heading = changeHeading(heading,-value)
        if (inst == 'R'):
            #Action R means to turn right the given number of degrees.
            heading = changeHeading(heading,+value)
        if (inst == 'F'):
        #Action F means to move forward by the given value in the direction the ship is currently facing.
           (xPos,yPos) = moveInHeading(heading,value,(xPos,yPos))
        print("New position (%d,%d)"%(xPos,yPos))


def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    course = processInputFile(input_path)
    followCourse(course)

if __name__ == "__main__":

    mainTask()