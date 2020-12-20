import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import getTileIDs
from advent import Tile
from advent import checkAllPossibleArrangementsOf
from advent import writeAt
from advent import writeImageToFile

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadTestFile(self):
        tiles = processInputFile( os.path.join(os.path.dirname(__file__),"test_input_2.txt") )
        self.assertEqual([0000,2311,1951,1171,1427,1489,2473,2971,2729,3079],getTileIDs(tiles))
        
        outputArray = [['_' for i in range(12 * 8)] for j in range(12 * 8)]
        writeAt(outputArray,0,0,tiles[0],2)
        
        if False:
            i = 0
            for r in range(12):
                for c in range(12):
                    tile =tiles[0]
                    orientation = 1
                    writeAt(outputArray,r*8,c*8,tile,orientation)
                i=i+1

        writeImageToFile(outputArray)


if __name__ == '__main__':
    unittest.main()