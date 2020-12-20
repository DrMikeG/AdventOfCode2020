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

        assert len(id0Str) == 10
        assert len(id1Str) == 10
        assert len(id2Str) == 10
        assert len(id3Str) == 10


        self.default_edges.append(id0Str) #N
        self.default_edges.append(id1Str) #E
        self.default_edges.append(id2Str) #S
        self.default_edges.append(id3Str) #W

    def getCharsArrays(self):
        assert len(self.default_edges) == 4
        return self.default_edges

    def getReversedCharsArrays(self):
        N_E_S_W_Edges = self.default_edges
        return [N_E_S_W_Edges[0][::-1],N_E_S_W_Edges[1][::-1],N_E_S_W_Edges[2][::-1],N_E_S_W_Edges[3][::-1]]


    def processsLinesIntoDefaultEdges(self,lines):
        # Get the 4 border strings into self.default_edges
        self.calcCharsArrayFromLines(lines)

    def calculateRotations(self):
        # process default edges to make 8 permutations
        # First entry
        # Default edge strings (read left-right, top-bottom)
        N_E_S_W_Edges = self.default_edges
        
        # Reversed edge strings (read right-left, bottom-top)
        rN_E_S_W_Edges = self.getReversedCharsArrays()

        allEdges = N_E_S_W_Edges + rN_E_S_W_Edges
        assert len(allEdges) == len(set(allEdges)) # all edges are unique


        ## N S E W
        self.rotations.append( [ 
            self.charStringToInt( N_E_S_W_Edges[0]),
            self.charStringToInt( N_E_S_W_Edges[1]),
            self.charStringToInt( N_E_S_W_Edges[2]),
            self.charStringToInt( N_E_S_W_Edges[3])
        ])
        ## If we rotate left (ESWN)
        self.rotations.append( [ 
            self.charStringToInt( N_E_S_W_Edges[1]),
            self.charStringToInt( rN_E_S_W_Edges[2]), # Flip
            self.charStringToInt( N_E_S_W_Edges[3]),
            self.charStringToInt( rN_E_S_W_Edges[0]) # Flip
        ])
        ## If we rotate left (SWNE)
        self.rotations.append( [ 
            self.charStringToInt( rN_E_S_W_Edges[2]), # Flip
            self.charStringToInt( rN_E_S_W_Edges[3]), # Flip
            self.charStringToInt( rN_E_S_W_Edges[0]), # Flip
            self.charStringToInt( rN_E_S_W_Edges[1]) # Flip
        ])
        ## If we rotate left (WNES)
        self.rotations.append( [ 
            self.charStringToInt( rN_E_S_W_Edges[3]), # Flip
            self.charStringToInt(  N_E_S_W_Edges[0]),
            self.charStringToInt( rN_E_S_W_Edges[1]), # Flip
            self.charStringToInt(  N_E_S_W_Edges[2])
        ])

        # Now we flip the original solution vertically
        # SENW
        self.rotations.append( [ 
            self.charStringToInt( N_E_S_W_Edges[2]),
            self.charStringToInt( rN_E_S_W_Edges[1]),
            self.charStringToInt( N_E_S_W_Edges[0]),
            self.charStringToInt( rN_E_S_W_Edges[3])
        ])
        # If we rotate left (ENWS)
        self.rotations.append( [ 
            self.charStringToInt( rN_E_S_W_Edges[1]),
            self.charStringToInt( rN_E_S_W_Edges[0]),
            self.charStringToInt( rN_E_S_W_Edges[3]),
            self.charStringToInt( rN_E_S_W_Edges[2])
        ])
        # If we rotate left (NWSE)
        self.rotations.append( [ 
            self.charStringToInt( rN_E_S_W_Edges[0]),
            self.charStringToInt( N_E_S_W_Edges[3]),
            self.charStringToInt( rN_E_S_W_Edges[2]),
            self.charStringToInt( N_E_S_W_Edges[1])
        ])
        # If we rotate left (WSEN)
        self.rotations.append( [
            self.charStringToInt( N_E_S_W_Edges[3]),
            self.charStringToInt( N_E_S_W_Edges[2]),
            self.charStringToInt( N_E_S_W_Edges[1]),
            self.charStringToInt( N_E_S_W_Edges[0])
        ])

    def getRotations(self):
        return self.rotations

    def charToBinStr(self,charString):
        assert len(charString) == 10
        # ..#.#.#..#
        oneStr =charString.replace("#","1")
        zeroStr = oneStr.replace(".","0")
        assert len(zeroStr) == 10
        return zeroStr

    def charStringToInt(self,charString):
        return int(self.charToBinStr(charString),2)

    def getID(self):
        return self.id

    def getBorderBottom(self,rotation):
        assert rotation < 8
        assert len(self.rotations) == 8
        return self.rotations[rotation][2]

    def getBorderRight(self,rotation):
        assert rotation < 8
        assert len(self.rotations) == 8
        return self.rotations[rotation][1]

    def getBorderTop(self,rotation):
        assert rotation < 8
        assert len(self.rotations) == 8
        return self.rotations[rotation][0]

    def getBorderLeft(self,rotation):
        assert rotation < 8
        assert len(self.rotations) == 8
        return self.rotations[rotation][3]



def getTileIDs(tiles):
    tileIDs = []
    for tile in tiles:
        tileIDs.append(tile.getID())
    assert len(tileIDs) == len(set(tileIDs))
    return tileIDs

def findTileWithID(tiles,tileID):
    for tile in tiles:
        if tile.getID() == tileID:
            return tile

def checkAllPossibleArrangementsOf(tiles):
    # If there are n tiles
    foundMatch = False
    nOrdersTried = 0
    gridN = int(math.sqrt(len(tiles)))
    topLeftID = 0
    topRightID =0
    bottomLeftID = 0
    bottomRightID = 0

    
    for uniqueOrder in permutations(tiles,len(tiles)):

        # The corner IDs are not dependent on rotation:
        if (gridN == 3):
            topLeftID = uniqueOrder[0].getID()
            topRightID = uniqueOrder[2].getID()
            bottomLeftID = uniqueOrder[7].getID()
            bottomRightID = uniqueOrder[8].getID()
        elif (gridN == 12):
            topLeftID = uniqueOrder[0].getID()
            topRightID = uniqueOrder[11].getID()
            bottomLeftID = uniqueOrder[132].getID()
            bottomRightID = uniqueOrder[143].getID()

        chosenRotations = {}
        #piece 1 has 8 starting positions
        for rotation in range(8):
            #print("Trying rotation %d of piece %d as piece 1"%(rotation,uniqueOrder[0].getID()))
            chosenRotations.clear()
            chosenRotations[0] = rotation

            #print("North == %d"%(uniqueOrder[0].getBorderTop(rotation)))
            #print("East == %d"%(uniqueOrder[0].getBorderRight(rotation)))
            #print("South == %d"%(uniqueOrder[0].getBorderBottom(rotation)))
            #print("West == %d"%(uniqueOrder[0].getBorderLeft(rotation)))

            # Try to fit every other tile for each of it's orientation
            # Is there ever more than one matching edge?

            # For every possible rotation of every tile, is there a solution?
            tileN = 0
            for tile in uniqueOrder:

                if tileN == 0:
                    tileN = tileN + 1
                    continue # first tile always matches

                bordersToCheck = ['top','left'] # Top and Left borders to test

                if tileN < gridN:
                    # first row
                    bordersToCheck = ['left'] #  Left only
                if tileN % gridN == 0:
                    # first colomn
                    bordersToCheck = ['top'] # Top only

                mustMatch = {}
                if 'top' in bordersToCheck:
                    # What is the border above?
                    tileAbove = tileN - gridN
                    rotationAbove = chosenRotations[tileAbove]
                    mustMatch['top'] = uniqueOrder[tileAbove].getBorderBottom(rotationAbove)
                if 'left' in bordersToCheck:
                    # What is the border above?
                    tileLeft = tileN - 1
                    rotationLeft = chosenRotations[tileLeft]
                    #print("Right == %d"%(uniqueOrder[0].getBorderRight(rotation)))
                    #print("Bottom == %d"%(uniqueOrder[tileLeft].getBorderBottom(rotationLeft)))
                    #print("Right == %d"%(uniqueOrder[0].getBorderRight(rotation)))
                    #print("Bottom == %d"%(uniqueOrder[tileLeft].getBorderBottom(rotationLeft)))
                    mustMatch['left'] = uniqueOrder[tileLeft].getBorderRight(rotationLeft)

                # Is there any rotation of this tile which matches?
                fittedPiece = False
                fittedOrientation = 0
                for tryFittingRotation in range(8):
                    fittedLeft = True
                    fittedTop = True
                    if 'left' in mustMatch:
                        nextTileRLeft = tile.getBorderLeft(tryFittingRotation)
                        if nextTileRLeft != mustMatch['left']:
                            fittedLeft = False
                            continue
                    if 'top' in mustMatch:
                        if tile.getBorderTop(tryFittingRotation) != mustMatch['top']:
                            fittedTop = False
                            continue
                    if fittedLeft and fittedTop:
                        fittedPiece = True
                        fittedOrientation = tryFittingRotation
                        #print("Can place piece %d orientation %d"%(tileN,fittedOrientation))
                        break
                
                if (fittedPiece):
                    chosenRotations[tileN] = fittedOrientation
                    tileN = tileN + 1
                else:
                    #print("Could not fit piece %d in any orientation"%(tileN))
                    break
            
            if len(chosenRotations) == 9:
                # Found solution
                foundMatch = True
                ids = []
                for t in uniqueOrder:
                    ids.append(t.getID())
                print(ids)
                print(chosenRotations)
                print (topLeftID * topRightID * bottomLeftID * bottomRightID)
                return

        nOrdersTried = nOrdersTried + 1
        print("number of orders tried = %s"%(nOrdersTried))
    
    if foundMatch:
        print (topLeftID * topRightID * bottomLeftID * bottomRightID)
    
    return foundMatch

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

    gr =math.sqrt(len(tiles))
    print ("Grid is %d x %d"%(gr,gr))


    return tiles

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    tiles = processInputFile(input_path)
    checkAllPossibleArrangementsOf(tiles)



if __name__ == "__main__":

    mainTask()