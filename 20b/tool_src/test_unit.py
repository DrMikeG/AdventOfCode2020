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
        puzzle = checkAllPossibleArrangementsOf(tiles)
        n = 3
        outputArray = [['_' for i in range(n * 8)] for j in range(n * 8)]


        i = 0
        for r in range(n):
            for c in range(n):
                tile = puzzle['fitted'][i]
                orientation = puzzle['fittedOrientation'][i]
                writeAt(outputArray,r*8,c*8,tile,orientation)
                i=i+1
        writeImageToFile(outputArray)
        


if __name__ == '__main__':
    unittest.main()