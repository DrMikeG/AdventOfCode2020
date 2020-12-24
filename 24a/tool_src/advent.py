import os
import re
import copy
import math

# odd-r horizontal row layout shoves odd rows right
# [0,0][1,0][2,0][3,0][4,0][5,0][6,0]
#   [0,1][1,1][2,1][3,1][4,1][5,1][6,1]
# [0,2][1,2][2,2][3,2][4,2][5,2][6,2]


def convertDirectionToGridMovement(directionStr):
    if directionStr == "e":
        return (1,0)
    if directionStr == "w":
        return (-1,0)
    
    if directionStr == "se":
        return (0,1)
    if directionStr == "sw":
        return (-1,1)
    
    if directionStr == "ne":
        return (1,-1)
    if directionStr == "nw":
        return (0,-1)

    assert False

def nextTokenLength(line):
    position = 0
    if line[position] == "e" or line[position] == "w":
        return 1
    if line[position] == "n" or line[position] == "s":
        return 2

def convertLineDirectionToGridPosition(line):
    #Because the tiles are hexagonal, every tile has six neighbors: 
    # east, southeast, southwest, west, northwest, and northeast. 
    # These directions are given in your list, respectively, as 
    # e, 
    # w, 
    # se, sw,
    # nw, and ne.
    tile =[0,0]

    while len(line) > 0:
        chop = nextTokenLength(line)
        token = line[:chop]
        line =  line[chop:]
        move = convertDirectionToGridMovement(token)
        tile[0] += move[0]
        tile[1] += move[1]

    return (tile[0],tile[1])

def flipTilePosition(tiles,tilePosition):
    if tilePosition in tiles:
        if tiles[tilePosition] == "Black":
            tiles[tilePosition] = "White"
        elif tiles[tilePosition] == "White":
            tiles[tilePosition] = "Black"
    else:
        tiles[tilePosition] = "Black"

def countBlack(tiles):
    count = 0
    for k in tiles:
        if tiles[k] == "Black":
            count += 1
    return count

def processInputFile(filePath):
    
    tiles = {}
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            tilePosition = convertLineDirectionToGridPosition(x.strip())
            flipTilePosition(tiles,tilePosition)
        f.close()
    else :
        print("%s does not exist"%(filePath))

    count = countBlack(tiles)
    print(count)
    return count

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    processInputFile(input_path)

if __name__ == "__main__":

    mainTask()
