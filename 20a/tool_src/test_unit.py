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
        self.assertEqual(1,len(rotations))
        defaultRotation = rotations[0]
        self.assertEqual(4,len(defaultRotation))        
        self.assertEqual(int("0011010010",2),defaultRotation[0]) # 210
        self.assertEqual(int("0001011001",2),defaultRotation[1]) # 89
        self.assertEqual(int("0011100111",2),defaultRotation[2]) #231
        self.assertEqual(int("0111110010",2),defaultRotation[3]) # 498











if __name__ == '__main__':
    unittest.main()