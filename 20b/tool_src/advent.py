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
        self.lines = lines.copy()

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
        #assert len(allEdges) == len(set(allEdges)) # all edges are unique


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

    def getLines(self):
        return self.lines

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



def collectCorners(tiles,puzzle):
    gridN = int(math.sqrt(len(tiles)))
    # The corner IDs are not dependent on rotation:
    if (gridN == 3):
        topLeftID = puzzle['fitted'][0].getID()
        topRightID = puzzle['fitted'][2].getID()
        bottomLeftID = puzzle['fitted'][7].getID()
        bottomRightID = puzzle['fitted'][8].getID()
    elif (gridN == 12):
        topLeftID = puzzle['fitted'][0].getID()
        topRightID = puzzle['fitted'][11].getID()
        bottomLeftID = puzzle['fitted'][132].getID()
        bottomRightID = puzzle['fitted'][143].getID()
    print (topLeftID * topRightID * bottomLeftID * bottomRightID)


def canFitTileInPositionAndOrientation(tiles,tile,orientation,position,puzzle):

    if position == 0:
        return True # can always fit the first tile
    
    gridN = int(math.sqrt(len(tiles)))

    bordersToCheck = ['top','left'] # Top and Left borders to test

    if position < gridN:
        # first row
        bordersToCheck = ['left'] #  Left only
    if position % gridN == 0:
        # first colomn
        bordersToCheck = ['top'] # Top only

    matches = True

    if 'top' in bordersToCheck:
        # What is the border above?
        tileAbove = puzzle['fitted'][position - gridN]
        rotationAbove = puzzle['fittedOrientation'][position - gridN]
        matches = (tile.getBorderTop(orientation) == tileAbove.getBorderBottom(rotationAbove))

    if matches:
        if 'left' in bordersToCheck:
            # What is the border above?
            tileLeft = puzzle['fitted'][position - 1]
            rotationLeft = puzzle['fittedOrientation'][position - 1]
            matches = (tile.getBorderLeft(orientation) == tileLeft.getBorderRight(rotationLeft))

    return matches

def canFitRemainingTiles(tiles,puzzle):
    # Some times have been fitted
    pos = puzzle['pos']
    #print("The next position to fill is %d"%(pos))
    remainingTiles = tiles.copy()
    #print("%d tiles"%(len(remainingTiles)))
    for used in puzzle['fitted']:
        remainingTiles.remove(puzzle['fitted'][used])
        #print("%d tiles still to fit"%(len(remainingTiles)))

    if len(remainingTiles) == 0:
        return True

    for nextTile in remainingTiles:
        for rotation in range(8):
            #print("Testing nexttile %d in orientation %d in positions %s"%(nextTile.getID(),rotation,pos))
            #N=nextTile.getBorderTop(rotation)
            #E=nextTile.getBorderRight(rotation)
            #S=nextTile.getBorderBottom(rotation)
            #W=nextTile.getBorderLeft(rotation)
            #print(list([N,E,S,W]))
            #if [1,2311,231, 616, 210, 318] == [pos,nextTile.getID(),N,E,S,W]:
            #    print(list([N,E,S,W]))
            #elif [2,2799,710, 9] == [pos,nextTile.getID(),N,E]:
            #    print(list([N,E,S,W]))

            if not canFitTileInPositionAndOrientation(tiles,nextTile,rotation,pos,puzzle):
                continue
            else:
                # Descend
                puzzle['fitted'][pos] = nextTile
                puzzle['fittedOrientation'][pos] = rotation
                puzzle['pos'] = pos + 1
                if canFitRemainingTiles(tiles,puzzle):
                    return True
                else:
                    # back track
                    puzzle['fitted'].pop(pos)
                    puzzle['fittedOrientation'].pop(pos)
                    puzzle['pos'] = pos

    return False

def checkAllPossibleArrangementsOf(tiles):


    puzzle = {'fitted' : {}, 'fittedOrientation' : {}, 'pos' : 0}

    for firstTile in tiles:
        for rotation in range(8):
            print("Testing first tile %d in orientation %d in positions %s"%(firstTile.getID(),rotation,0))
            
            #N=firstTile.getBorderTop(rotation)
            #E=firstTile.getBorderRight(rotation)
            #S=firstTile.getBorderBottom(rotation)
            #W=firstTile.getBorderLeft(rotation)
            #print(list([N,E,S,W]))
            #if [1951,564, 318, 710, 587] == [firstTile.getID(),N,E,S,W]:
                #print(list([N,E,S,W]))
            


            puzzle['fitted'][0] = firstTile
            puzzle['fittedOrientation'][0] = rotation
            puzzle['pos'] = 1

            if canFitRemainingTiles(tiles,puzzle):
                collectCorners(tiles,puzzle)
                return puzzle
            else:
                # back track
                puzzle['fitted'].pop(0)
                puzzle['fittedOrientation'].pop(0)
                puzzle['pos'] = 0
           

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



def rotate90(original):
    rotated = list(zip(*original[::-1]))
    return rotated

def rotate180(original):
    return rotate90(rotate90(original))

def rotate270(original):
    return rotate90(rotate90(rotate90(original)))





def writeAt(outputArray,cBase,rBase,tile,orientation):

    if orientation == 0:
        # simple write
        lines = tile.getLines()
        assert len(lines) == 11
        r = 0
        for dirtyLine in lines[2:-1:]:
            c = 0
            cleanLine = dirtyLine.strip()
            assert len(cleanLine) == 10
            for ch in cleanLine[1:-1]:
                outputArray[rBase+r][cBase+c] = ch
                c = c + 1
            r = r + 1
    
    if orientation == 1:
        smallOutputArray = [['_' for i in range(8)] for j in range(8)]
        lines = tile.getLines()
        assert len(lines) == 11
        r = 0
        for dirtyLine in lines[2:-1:]:
            c = 0
            cleanLine = dirtyLine.strip()
            assert len(cleanLine) == 10
            for ch in cleanLine[1:-1]:
                smallOutputArray[r][c] = ch
                c = c + 1
            r = r + 1
        smallOutputArray = rotate270(smallOutputArray)
        for r in range(8):
            for c in range(8):
                outputArray[rBase+r][cBase+c] = smallOutputArray[r][c]
    
    if orientation == 2:
        smallOutputArray = [['_' for i in range(8)] for j in range(8)]
        lines = tile.getLines()
        assert len(lines) == 11
        r = 0
        for dirtyLine in lines[2:-1:]:
            c = 0
            cleanLine = dirtyLine.strip()
            assert len(cleanLine) == 10
            for ch in cleanLine[1:-1]:
                smallOutputArray[r][c] = ch
                c = c + 1
            r = r + 1
        smallOutputArray = rotate180(smallOutputArray)
        for r in range(8):
            for c in range(8):
                outputArray[rBase+r][cBase+c] = smallOutputArray[r][c]
    else:
        # simple write
        lines = tile.getLines()
        assert len(lines) == 11
        r = 0
        for dirtyLine in lines[2:-1:]:
            c = 0
            cleanLine = dirtyLine.strip()
            assert len(cleanLine) == 10
            for ch in cleanLine[1:-1]:
                outputArray[rBase+r][cBase+c] = ch
                c = c + 1
            r = r + 1

def writeImageToFile(outputArray):
    f = open(os.path.join(os.path.dirname(__file__),"output.txt"), "w")
    for line in outputArray:
        # write line to output file
        for c in line:
            f.write(c)
        f.write("\n")
    f.close()


def mainTask():
    input_path = getInputPath()
    tiles = processInputFile(input_path)
    puzzle = checkAllPossibleArrangementsOf(tiles)

    # 80 x 80
    #x = [[foo for i in range(10)] for j in range(10)]
    # x is now a 10x10 array of 'foo' (which can depend on i and j if you want)

    outputArray = [['_' for i in range(12 * 8)] for j in range(12 * 8)]

    i = 0
    for r in range(12):
        for c in range(12):
            tile = puzzle['fitted'][i]
            orientation = puzzle['fittedOrientation'][i]
            writeAt(outputArray,r*8,c*8,tile,orientation)
            i=i+1



if __name__ == "__main__":

    mainTask()