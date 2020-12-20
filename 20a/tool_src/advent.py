import os
import re
import copy
import math

# There are 144 tiles
# I am pretty sure there are only 8 possible rotations for each tile
# N,E,S,W,NR,ER,SR,WE
# Edge indices count clockwise from North [0,1,2,3]

#Load tiles
#For each time, enumerate its 8 possible rotations
#Manually check one tile


class Tile:
    

    def __init__(self, lines):
        self.default_edges = []
        self.rotations = []
        self.id = -1
        assert len(lines) == 11
        assert len(lines[0]) == 10
        self.parseTileID(lines[0])
        self.processsLinesIntoDefaultEdges(lines)
        self.calculateRotations()

    def parseTileID(self,line0):
        #"Tile 2297:"
        self.id = int(line0.strip().split(" ")[1].split(":")[0])


    def calcCharsArrayFromLines(self,lines):
        # 2nd line is ID 0
        # 11th line is ID 2
        # Last column of 2nd - 11th line is ID 1
        # First column of 2nd - 11th line is ID 3

        id0Str = ""
        id1Str = ""
        id2Str = ""
        id3Str = ""
        for r in range(0,10):
            id0Str = id0Str + lines[1][r]
        for r in range(1,11):
            id1Str = id1Str + lines[r][9]
        for r in range(0,10):
            id2Str = id2Str + lines[10][r]
        for r in range(1,11):
            id3Str = id3Str + lines[r][0]
        
        self.default_edges.append(id0Str)
        self.default_edges.append(id1Str)
        self.default_edges.append(id2Str)
        self.default_edges.append(id3Str)

    def getCharsArrays(self):
        assert len(self.default_edges) == 4
        return self.default_edges

    def processsLinesIntoDefaultEdges(self,lines):
        # Get the 4 border strings into self.default_edges
        self.calcCharsArrayFromLines(lines)

    def defaultFourInts(self):
        fourInts = []
        for st in self.default_edges:
            fourInts.append(self.charStringToInt(st))
        return fourInts

    def calculateRotations(self):
        # process default edges to make 8 permutations
        # First entry
        self.rotations.append(self.defaultFourInts())
    
    def getRotations(self):
        return self.rotations

    def charStringToInt(self,charString):
        assert len(charString) == 10
        # ..#.#.#..#
        oneStr =charString.replace("#","1")
        zeroStr = oneStr.replace(".","0")
        return int(zeroStr,2)

    def getID(self):
        return self.id


def getTileIDs(tiles):
    tileIDs = []
    for tile in tiles:
        tileIDs.append(tile.getID())
    assert len(tileIDs) == len(set(tileIDs))
    return tileIDs


def processLineOfInputIntoRuleStruct(line,rules):
    # "1: 2 3 | 3 2"
    # A is -1
    # B is -2
    partsA = line.split(":")                # ["1","2 3 | 3 2"]
    assert len(partsA) == 2
    partsB = partsA[1].strip().split("|")   # '["2 3","3 2"]
    ruleInt = int(partsA[0].strip())
    for optionsStr in partsB:
        optionIntArray = []
        rulesInOption = optionsStr.strip().split(" ") # ["2","3"]
        for optionStr in rulesInOption:
            if optionStr.strip() == "\"a\"":
                optionIntArray.append(-1)
            elif optionStr.strip() == "\"b\"":
                optionIntArray.append(-2)
            else:
                optionIntArray.append(int(optionStr))
        if ruleInt not in rules:
            rules[ruleInt] = []
        rules[ruleInt].append(optionIntArray)


def processInputFile(filePath):

    tiles = []

    if os.path.exists(filePath):
        f = open(filePath, "r")

        linesToProcess = []

        for x in f:
            if x == "\n":
                tiles.append( Tile(linesToProcess) )
                linesToProcess.clear()
                continue
            else:
                linesToProcess.append(x.strip())
        f.close()
        if len(linesToProcess) > 0:
            tiles.append( Tile(linesToProcess) )
    else :
        print("%s does not exist"%(filePath))

    return tiles

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    tiles = processInputFile(input_path)
    

if __name__ == "__main__":

    mainTask()