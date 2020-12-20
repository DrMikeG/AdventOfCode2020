import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import getTileIDs
from advent import Tile

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
        rotations = tiles[0].getRotations()
        self.assertEqual(4,len(rotations))

        defaultRotation = rotations[0]
        self.assertEqual(4,len(defaultRotation))
        self.assertEqual(int("0011010010",2),defaultRotation[0]) # 210 N
        self.assertEqual(int("0001011001",2),defaultRotation[1]) # 89  E
        self.assertEqual(int("0011100111",2),defaultRotation[2]) #231  S
        self.assertEqual(int("0111110010",2),defaultRotation[3]) # 498 W

        ESWN = rotations[1]
        self.assertEqual(4,len(ESWN))
        self.assertEqual(int("0001011001",2),ESWN[0]) # 89  E
        self.assertEqual(int("1110011100",2),ESWN[1]) # 924  rS
        self.assertEqual(int("0111110010",2),ESWN[2]) # 498 W
        self.assertEqual(int("0100101100",2),ESWN[3]) # 300 rN

        SWNE = rotations[2]
        self.assertEqual(4,len(SWNE))
        self.assertEqual(int("1110011100",2),SWNE[0]) # 924 rS
        self.assertEqual(int("1011000001",2),SWNE[1]) # 705 rW
        self.assertEqual(int("0100101100",2),SWNE[2]) # 300 N
        self.assertEqual(int("0001011001",2),SWNE[3]) # 89  E
        









if __name__ == '__main__':
    unittest.main()