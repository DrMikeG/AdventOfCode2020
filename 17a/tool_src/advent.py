import os
import re
import copy
import math

g_sparse_grid = {}

def clearGrid():
    g_sparse_grid.clear()


# grid is a sparse structure
def setCell(x,y,z,state):
    g_sparse_grid[(x,y,z)] = state

def isCellActive(x,y,z):

    if (x,y,z) in g_sparse_grid:
        return g_sparse_grid[x,y,z] == True
    return False

def getBoundingBox():
    minX = 0
    minY = 0
    minZ = 0
    maxX = 0
    maxY = 0
    maxZ = 0
    for pos in g_sparse_grid:
        assert len(pos) == 3
        if pos[0] < minX :
            minX = pos[0]
        if pos[1] < minY :
            minY = pos[1]
        if pos[2] < minZ :
            minZ = pos[2]
        if pos[0] > maxX :
            maxX = pos[0]
        if pos[1] > maxY :
            maxY = pos[1]
        if pos[2] > maxZ :
            maxZ = pos[2]
    return (minX,minY,minZ,maxX,maxY,maxZ)


def countActive():
    count = 0
    for pos in g_sparse_grid:
        if isCellActive(pos[0],pos[1],pos[2]) :
            count = count + 1
    return count

def countActiveNeighboursIn3x3x3(x,y,z):
    count = 0
    for xd in [-1,0,1]:
        for yd in [-1,0,1]:
            for zd in [-1,0,1]:
                # Don't check your own square (x,y,z)
                if (xd == 0) and (yd == 0) and (zd == 0):
                    continue
                if isCellActive(x+xd,y+yd,z+zd) :
                    count = count + 1
    return count

def cycle():
    boundingBox = getBoundingBox()

    newDict = {}
    #If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    #If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

    for z in range(boundingBox[2]-1,boundingBox[5]+2):          # for each slice
        for y in range(boundingBox[1]-1,boundingBox[4]+2):      # for each row
            for x in range(boundingBox[0]-1,boundingBox[3]+2):  # for each col
                if isCellActive(x,y,z):
                    # if exactly 2 or 3 of its neighbors are also active, the cube remains active
                    countD = countActiveNeighboursIn3x3x3(x,y,z)
                    if (countD == 2) or (countD == 3):
                        newDict[(x,y,z)] = True
                else:
                    # if exactly 3 of its neighbors are active, the cube becomes active
                    countD = countActiveNeighboursIn3x3x3(x,y,z)
                    if (countD == 3):
                        newDict[(x,y,z)] = True

    # swap g_sparse_grid with newDict
    clearGrid()
    g_sparse_grid.update(newDict)
    return True

def printBoundingBox():
    print("\n---------\n")
    boundingBox = getBoundingBox()
    for z in range(boundingBox[2],boundingBox[5]+1):
        print("\nz=%d"%(z))
        for y in range(boundingBox[1],boundingBox[4]+1):
            rowStr = ""
            for x in range(boundingBox[0],boundingBox[3]+1):
                if isCellActive(x,y,z):
                    rowStr = rowStr + "#"
                else:
                    rowStr = rowStr + "."
            print(rowStr)
    print("\n--------\n")

def doCycles(nCycles):
    for _ in range(nCycles):
        cycle()

def processLineOfInputIntoStruct(l,x,y,z):
    # This is for slice Z (fixed)
    # This is row Y (fixed)
    # For each character set x
    assert(x == 0)
    #.###.#.#
    for i in range(len(l)):
        if l[i] == "." :
            setCell(x,y,z,False)
        elif l[i] == "#" :
            setCell(x,y,z,True)
        x = x + 1

def processInputFile(filePath):
    clearGrid()
    x = 0 # across the grid
    y = 0 # up and down a level of the grid
    z = 0 # height up and down stack
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for l in f:
            x = 0
            processLineOfInputIntoStruct(l.strip(),x,y,z)
            y = y + 1
        f.close()
    else :
        print("%s does not exist"%(filePath))

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    processInputFile(input_path)
    doCycles(6)
    print(countActive())

if __name__ == "__main__":

    mainTask()