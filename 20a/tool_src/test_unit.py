import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import getTileIDs
from advent import Tile
from advent import checkAllPossibleArrangementsOf

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadTestFile(self):
        tiles = processInputFile( os.path.join(os.path.dirname(__file__),"test_input_2.txt") )
        self.assertEqual([2311,1951,1171,1427,1489,2473,2971,2729,3079],getTileIDs(tiles))
        self.assertEqual(2311,tiles[0].getID())
        charArrays = tiles[0].getCharsArrays()
        self.assertEqual(charArrays[0],"..##.#..#.")
        self.assertEqual(charArrays[1],"...#.##..#")
        self.assertEqual(charArrays[2],"..###..###")
        self.assertEqual(charArrays[3],".#####..#.")
        
        rCharArrays = tiles[0].getReversedCharsArrays()
        self.assertEqual(rCharArrays[0],".#..#.##..")
        self.assertEqual(rCharArrays[1],"#..##.#...")
        self.assertEqual(rCharArrays[2],"###..###..")
        self.assertEqual(rCharArrays[3],".#..#####.")

        self.assertEqual("0011010010",tiles[0].charToBinStr(charArrays[0]))
        self.assertEqual("0001011001",tiles[0].charToBinStr(charArrays[1]))
        self.assertEqual("0011100111",tiles[0].charToBinStr(charArrays[2]))
        self.assertEqual("0111110010",tiles[0].charToBinStr(charArrays[3]))

        self.assertEqual("0100101100",tiles[0].charToBinStr(rCharArrays[0]))
        self.assertEqual("1001101000",tiles[0].charToBinStr(rCharArrays[1]))
        self.assertEqual("1110011100",tiles[0].charToBinStr(rCharArrays[2]))
        self.assertEqual("0100111110",tiles[0].charToBinStr(rCharArrays[3]))

        self.assertEqual(int("0011010010",2),tiles[0].charStringToInt(charArrays[0]))
        self.assertEqual(int("0001011001",2),tiles[0].charStringToInt(charArrays[1]))
        self.assertEqual(int("0011100111",2),tiles[0].charStringToInt(charArrays[2]))
        self.assertEqual(int("0111110010",2),tiles[0].charStringToInt(charArrays[3]))

        self.assertEqual(int("0100101100",2),tiles[0].charStringToInt(rCharArrays[0]))
        self.assertEqual(int("1001101000",2),tiles[0].charStringToInt(rCharArrays[1]))
        self.assertEqual(int("1110011100",2),tiles[0].charStringToInt(rCharArrays[2]))
        self.assertEqual(int("0100111110",2),tiles[0].charStringToInt(rCharArrays[3]))

        self.assertEqual(210,tiles[0].charStringToInt(charArrays[0]))
        self.assertEqual(89,tiles[0].charStringToInt(charArrays[1]))
        self.assertEqual(231,tiles[0].charStringToInt(charArrays[2]))
        self.assertEqual(498,tiles[0].charStringToInt(charArrays[3]))

        self.assertEqual(300,tiles[0].charStringToInt(rCharArrays[0]))
        self.assertEqual(616,tiles[0].charStringToInt(rCharArrays[1]))
        self.assertEqual(924,tiles[0].charStringToInt(rCharArrays[2]))
        self.assertEqual(318,tiles[0].charStringToInt(rCharArrays[3]))

        rotations = tiles[0].getRotations()
        self.assertEqual(8,len(rotations))

        defaultRotation = rotations[0]
        self.assertEqual(4,len(defaultRotation))
        N = 210
        E = 89
        S = 231
        W = 498
        rN = 300
        rE = 616
        rS = 924
        rW = 318

        self.assertEqual(N,tiles[0].charStringToInt(charArrays[0]))
        self.assertEqual(E,tiles[0].charStringToInt(charArrays[1]))
        self.assertEqual(S,tiles[0].charStringToInt(charArrays[2]))
        self.assertEqual(W,tiles[0].charStringToInt(charArrays[3]))

        # The 8 cycles should be
        #  N,E,S,W
        #  E,rS,W,rN
        # rS,rW,rN,rE
        # rW,N,rE,S

        # S,rE,N,rW
        # rE,rN,rW,rS
        # rN,W,rS,E
        # W,S,E,N

        self.assertEqual([N,E,S,W],rotations[0])
        self.assertEqual([ E,rS,W,rN],rotations[1])
        self.assertEqual([rS,rW,rN,rE],rotations[2])
        self.assertEqual([rW,N,rE,S],rotations[3])

        self.assertEqual([S,rE,N,rW],rotations[4])
        self.assertEqual([rE,rN,rW,rS],rotations[5])
        self.assertEqual([rN,W,rS,E],rotations[6])
        self.assertEqual([W,S,E,N],rotations[7])

        allNumbers =[]
        for tile in tiles:
            chars = tile.getCharsArrays()
            for c in chars:
                allNumbers.append(tile.charStringToInt(c))
            rchars = tile.getReversedCharsArrays()
            for c in rCharArrays:
                allNumbers.append(tile.charStringToInt(c))
        print(allNumbers)

        singularNumbers = []
        for s in allNumbers:
            c = allNumbers.count(s)
            print("number %d count %d"%(s,c))
            if c == 1:
                singularNumbers.append(s)
        print("only occur once %s"%(list(singularNumbers)))

        ## Corner tiles will have 4 singular numbers
        
        for tile in tiles:
            allTileNumbers =[]
            chars = tile.getCharsArrays()
            for c in chars:
                allTileNumbers.append(tile.charStringToInt(c))
            rchars = tile.getReversedCharsArrays()
            for c in rCharArrays:
                allTileNumbers.append(tile.charStringToInt(c))
            nSingular = 0
            for a in allTileNumbers:
                if a in singularNumbers:
                    nSingular = nSingular + 1
            if nSingular > 2:
                print("Corner tile %d"%(tile.getID()))

        ##checkAllPossibleArrangementsOf(tiles)




if __name__ == '__main__':
    unittest.main()