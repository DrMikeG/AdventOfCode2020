import os
import re
import copy

def printGrid(grid):
    print()
    for row in grid:
        print(row)

FLOOR = 0
EMPTY = 1
OCCUPIED = 2
# 0 is floor
# 1 is empty
# 2 is occupied

def processLineOfInputIntoStruct(line,grid,rowNumber):

    #assert len(line) == 93
    #assert len(line) == 10
    gridRow = []
    lineS = line.strip()
    for element in lineS:
        gridRow.append(EMPTY)
        if (element == '.'):
            gridRow[-1] = FLOOR
        if (element == '#'):
            gridRow[-1] = OCCUPIED
    grid.append(gridRow)

def processInputFile(filePath):
    
    grid = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        row = 0
        for x in f:
            processLineOfInputIntoStruct(x,grid,row)
            row = row + 1
        f.close()
    else :
        print("%s does not exist"%(filePath))

    return grid

def countOccupiedInGrid(grid):
    count = 0
    for row in grid:
        for col in row:
            if (col == OCCUPIED):
                count = count + 1
    return count

def countOccupiedIn8(grid,r,c):
    countOf2 = 0
    for rd in [-1,0,1]:
        for cd in [-1,0,1]:
            if (rd == 0 and cd == 0):
                continue
            if isFirstSeatInDirOccupied(grid,r,c,rd,cd) == OCCUPIED:
                countOf2 += 1
    return countOf2

def isFirstSeatInDirOccupied(grid,r,c,rowStep,colStep):
    ## From grid[r][c] walk in direction [x,y] until you reach a gridcell that is not FLOOR
    ## Return true if that grid cell is OCCUPIED
    assert not (rowStep == colStep == 0)
    rowMax = len(grid)
    colMax = len(grid[0])

    steps = 1
    occ = FLOOR

    keepSteping = True
    while keepSteping:
        # next cell to check would be
        rd = rowStep * steps
        cd = colStep * steps
        rToCheck= r+rd
        cToCheck= c+cd
        if(rToCheck < 0):
            keepSteping = False
            continue
        if(cToCheck < 0):
            keepSteping = False
            continue
        if(rToCheck >= rowMax):
            keepSteping = False
            continue
        if(cToCheck >= colMax):
            keepSteping = False
            continue        
        if grid[rToCheck][cToCheck] != FLOOR:
            occ = grid[rToCheck][cToCheck]
            keepSteping = False
        steps = steps + 1
    return occ

def stepGrid(grid):

    nChages = 0
    outputGrid = copy.deepcopy(grid)

    rowMax = len(grid)
    colMax = len(grid[0])

    for r in range(0,rowMax):
        for c in range(0,colMax):
            occupiedNeigbours = countOccupiedIn8(grid,r,c)
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if (grid[r][c] == EMPTY) and (occupiedNeigbours == 0):
                outputGrid[r][c] = OCCUPIED
                nChages = nChages + 1
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            if (grid[r][c] == OCCUPIED) and (occupiedNeigbours > 4):
                outputGrid[r][c] = EMPTY
                nChages = nChages + 1

    return (nChages,outputGrid)
    

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    grid = processInputFile(input_path)

    nChanges = 1
    while nChanges > 0:
        (nChanges,grid) = stepGrid(grid)
        print(countOccupiedInGrid(grid))

if __name__ == "__main__":

    mainTask()