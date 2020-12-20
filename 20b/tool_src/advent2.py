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

def writeImageToFile(outputArray):
    f = open(os.path.join(os.path.dirname(__file__),"my_monster_output.txt"), "a")
    for line in outputArray:
        # write line to output file
        for c in line:
            f.write(c)
        f.write("\n")
    f.close()

def processInputFile(filePath):

    image = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            imageRow = []
            for c in x.strip():
                imageRow.append(c)
            image.append(imageRow)
        f.close()
        
    else :
        print("%s does not exist"%(filePath))
    return image

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"output.txt")

def flipNorthToSouth(original):
    smallOutputArray = [['_' for i in range(20)] for j in range(20)]
    for r in range(20):
        for c in range(20):
            smallOutputArray[19-r][c] = original[r][c]
    return smallOutputArray

def rotate90(original):
    rotated = list(zip(*original[::-1]))
    return rotated

def rotate180(original):
    return rotate90(rotate90(original))

def rotate270(original):
    return rotate90(rotate90(rotate90(original)))

def seaMonsters():
    eigthSeaMonsters = []
    smallOutputArray = [[' ' for i in range(20)] for j in range(20)]
    str1 = "                  # "
    r = 9
    c = 0
    for ch in str1:
        smallOutputArray[r][c] = ch
        c = c + 1
    str2 = "#    ##    ##    ###"
    r = r+1
    c = 0
    for ch in str2:
        smallOutputArray[r][c] = ch
        c = c + 1
    str3 = " #  #  #  #  #  #   "
    r = r+1
    c = 0
    for ch in str3:
        smallOutputArray[r][c] = ch
        c = c + 1
    eigthSeaMonsters.append(smallOutputArray)
    eigthSeaMonsters.append(rotate90(smallOutputArray))
    eigthSeaMonsters.append(rotate180(smallOutputArray))
    eigthSeaMonsters.append(rotate270(smallOutputArray))
    smallOutputArray= flipNorthToSouth(smallOutputArray)
    eigthSeaMonsters.append(smallOutputArray)
    eigthSeaMonsters.append(rotate90(smallOutputArray))
    eigthSeaMonsters.append(rotate180(smallOutputArray))
    eigthSeaMonsters.append(rotate270(smallOutputArray))
    assert len(eigthSeaMonsters)==8
    return eigthSeaMonsters

def ifSeaMonsterMarkPositions(image,rBase,cBase,seaMonster):
    assert len(seaMonster) == 20
    assert len(seaMonster[0]) == 20
    imageWidth = len(image[0])-1
    imageHeight = len(image)-1
    toMark = []
    for r in range(20):
        for c in range(20):
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
        image[rc[0]][rc[1]] = "O"
    return True

def mainTask():
    input_path = getInputPath()
    image = processInputFile(input_path)
    assert len(image) == 96
    assert len(image[0]) == 96


    for s in seaMonsters():
        writeImageToFile(s)

    


if __name__ == "__main__":

    mainTask()