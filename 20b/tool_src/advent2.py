import os
import re
import copy
import math
from itertools import permutations

# There are 144 tiles
# I am pretty sure there are only 8 possible rotations for each tile
# N,E,S,W,NR,ER,SR,WE
# Edge indices count clockwise from North [0,1,2,3]

#Load tiles
#For each time, enumerate its 8 possible rotations
#Manually check one tile

def countHashes(outputArray):
    sum = 0
    for line in outputArray:
        for c in line:
            if c == "#":
                sum = sum + 1
    return sum

def writeImageToFile(outputArray):
    f = open(os.path.join(os.path.dirname(__file__),"my_monster_output.txt"), "w")
    for line in outputArray:
        # write line to output file
        for c in line:
            f.write(c)
        f.write("\n")
    f.close()

def flipNorthToSouth(original,sq):
    smallOutputArray = [['_' for i in range(sq)] for j in range(sq)]
    for r in range(sq):
        for c in range(sq):
            smallOutputArray[(sq-1)-r][c] = original[r][c]
    return smallOutputArray

def rotate90(original):
    rotated = list(zip(*original[::-1]))
    untuple = []
    for r in rotated:
        newR = []
        for c in r:
            newR.append(c)
        untuple.append(newR)
    return untuple

def rotate180(original):
    return rotate90(rotate90(original))

def rotate270(original):
    return rotate90(rotate90(rotate90(original)))

def processInputFile(filePath):

    image = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            imageRow = []
            for c in x.strip():
                imageRow.append(str(c))
            image.append(imageRow)
        f.close()
    else :
        print("%s does not exist"%(filePath))
    return image

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"output_without_borders.txt")

def seaMonsters():
    filePath = os.path.join(os.path.dirname(__file__),"my_monster_input.txt")
    f = open(filePath, "r")
    
    monsters = []
    monster = []
    for x in f:
        if x.strip() == "-":
            monsters.append(monster.copy())
            monster = []
        else:
            monsterRow = []
            for c in x:
                if not c == "\n":
                    monsterRow.append(c)
            monster.append(monsterRow)
    f.close()
    monsters.append(monster.copy())
    assert len(monsters)==8
    return monsters

def ifSeaMonsterMarkPositions(image,rBase,cBase,seaMonster):

    imageWidth = len(image[0])-1
    imageHeight = len(image)-1
    toMark = []
    for r in range(len(seaMonster)):
        for c in range(len(seaMonster[0])):
            if (seaMonster[r][c] =="#"):
                toMark.append((r+rBase,c+cBase))
                if (r+rBase < 0):
                    return False
                if (r+rBase > imageHeight):
                    return False
                if (c+cBase < 0):
                    return False
                if (c+cBase > imageWidth):
                    return False
                cell = image[r+rBase][c+cBase]
                if cell != "#" and cell != "O":
                    return False
    print("Found sea monster at (%d,%d)"%(rBase,cBase))
    for rc in toMark:
        r = rc[0]
        c = rc[1]
        image[r][c] = "O"
    return True

def mainTask():
    input_path = getInputPath()
    image = processInputFile(input_path)
    assert len(image) == 96
    assert len(image[0]) == 96



if __name__ == "__main__":

    mainTask()