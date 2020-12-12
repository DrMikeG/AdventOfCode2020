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

def rotate90(xOff,yOff):
    # A position X becomes a negative 
    newYOff = -xOff
    newXOff = yOff
    return (newXOff,newYOff)

def rotate180(xOff,yOff):
    (newXOff,newYOff) = rotate90(xOff,yOff)
    return rotate90(newXOff,newYOff)

def rotate270(xOff,yOff):
    (newXOff,newYOff) = rotate90(xOff,yOff)
    return rotate180(newXOff,newYOff)


def rotateM90(xOff,yOff):
    # A position X becomes a negative 
    newYOff = xOff
    newXOff = -yOff
    return (newXOff,newYOff)

def rotateM180(xOff,yOff):
    (newXOff,newYOff) = rotateM90(xOff,yOff)
    return rotateM90(newXOff,newYOff)

def rotateM270(xOff,yOff):
    (newXOff,newYOff) = rotateM90(xOff,yOff)
    return rotateM180(newXOff,newYOff)

def changeHeading(wayPointPos,shipPos,angleDelta):
    
    # Don't actually need to be able to cope with every angle
    # only 
    #-90
    #-180
    #-270
    #-90
    #-180
    #-270

    (wayPoint_xPos,wayPoint_yPos) = wayPointPos
    (ship_xPos,ship_yPos) = shipPos
    wayPointDeltaX = (wayPoint_xPos-ship_xPos)
    wayPointDeltaY = (wayPoint_yPos-ship_yPos)
    
    if(angleDelta == 90):
        # turn right 90
        (wayPointDeltaX,wayPointDeltaY) = rotate90(wayPointDeltaX,wayPointDeltaY)

    elif(angleDelta == 180):
        # turn right 180
        (wayPointDeltaX,wayPointDeltaY) = rotate180(wayPointDeltaX,wayPointDeltaY)

    elif(angleDelta == 270):
        # turn right 270
        (wayPointDeltaX,wayPointDeltaY) = rotate270(wayPointDeltaX,wayPointDeltaY)

    elif(angleDelta == -90):
        # turn left 90
        (wayPointDeltaX,wayPointDeltaY) = rotateM90(wayPointDeltaX,wayPointDeltaY)

    elif(angleDelta == -180):
        # turn left 180
        (wayPointDeltaX,wayPointDeltaY) = rotateM180(wayPointDeltaX,wayPointDeltaY)

    elif(angleDelta == -270):
        # turn left 270
        (wayPointDeltaX,wayPointDeltaY) = rotateM270(wayPointDeltaX,wayPointDeltaY)
    else:
        assert(False)

    wayPoint_xPos = wayPointDeltaX + ship_xPos # new position absolute
    wayPoint_yPos = wayPointDeltaY + ship_yPos # new position absolute

    return ((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos))



def moveInDirectionOfWayPointAndUpdateWayPoint(wayPointPos,shipPos,steps):
    (wayPoint_xPos,wayPoint_yPos) = wayPointPos
    (ship_xPos,ship_yPos) = shipPos
    
    wayPointDeltaX = (wayPoint_xPos-ship_xPos)
    wayPointDeltaY = (wayPoint_yPos-ship_yPos)

    changeX = wayPointDeltaX * steps
    changeY = wayPointDeltaY * steps

    ship_xPos = ship_xPos + changeX
    ship_yPos = ship_yPos + changeY
    wayPoint_xPos = wayPoint_xPos + changeX
    wayPoint_yPos = wayPoint_yPos + changeY
    return ((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos))

def distToWayPoint(wayPointPos,shipPos):
    (wayPoint_xPos,wayPoint_yPos) = wayPointPos
    (ship_xPos,ship_yPos) = shipPos
    wayPointDeltaX = (wayPoint_xPos-ship_xPos)
    wayPointDeltaY = (wayPoint_yPos-ship_yPos)
    dist = math.sqrt((wayPointDeltaX*wayPointDeltaX)+(wayPointDeltaY*wayPointDeltaY))
    return dist

def followCourse(course):

    # waypoint in absolute position, not relative to ship

    #waypoint starts 10 units east and 1 unit north
    wayPoint_xPos = 10
    wayPoint_yPos = 1

    #Ship starts facing East
    ship_xPos = 0
    ship_yPos = 0

    #when you move the ship, you move the waypoint
    #when you turn the ship, you turn the waypoint

    for (inst,value) in course:
        if (inst == 'N'):
            print ("Moving waypoint %s by %d"%(inst,value))
            #Action N means to move north by the given value.
            wayPoint_yPos += value
        if (inst == 'S'):
            print ("Moving waypoint %s by %d"%(inst,value))
            #Action S means to move south by the given value.
            wayPoint_yPos -= value
        if (inst == 'E'):
            print ("Moving waypoint %s by %d"%(inst,value))
            #Action E means to move east by the given value.
            wayPoint_xPos += value
        if (inst == 'W'):
            print ("Moving waypoint %s by %d"%(inst,value))
            #Action W means to move west by the given value.
            wayPoint_xPos -= value

        if (inst == 'L'):
            print ("Turning waypoint %s by %d"%(inst,value))
            #Action L means to turn left the given number of degrees.
            disB4 = distToWayPoint((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos))
            ((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos)) = changeHeading((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos),-value)
            disAft = distToWayPoint((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos))
            assert(disB4 == disAft)
        if (inst == 'R'):
            print ("Turning waypoint %s by %d"%(inst,value))
            #Action R means to turn right the given number of degrees.
            disB4 = distToWayPoint((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos))
            ((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos)) = changeHeading((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos),+value)
            disAft = distToWayPoint((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos))
            assert(disB4 == disAft)
        
        if (inst == 'F'):
            #Action F means to move forward by the given value in the direction the ship is currently facing.
            before_wayPointx_d = wayPoint_xPos-ship_xPos
            before_wayPointy_d = wayPoint_yPos-ship_yPos
            ((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos)) = moveInDirectionOfWayPointAndUpdateWayPoint((wayPoint_xPos,wayPoint_yPos),(ship_xPos,ship_yPos),value)
            print ("Moving ship %s by %d New ship position (%d,%d)"%(inst,value,ship_xPos,ship_yPos))
            after_wayPointx_d = wayPoint_xPos-ship_xPos
            after_wayPointy_d = wayPoint_yPos-ship_yPos
            assert(before_wayPointx_d ==after_wayPointx_d)
            assert(before_wayPointy_d ==after_wayPointy_d)

        print("Waypoint position (%d,%d)"%(wayPoint_xPos-ship_xPos,wayPoint_yPos-ship_yPos))


def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    course = processInputFile(input_path)
    followCourse(course)

if __name__ == "__main__":

    mainTask()