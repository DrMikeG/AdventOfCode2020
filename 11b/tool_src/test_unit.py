import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import isFirstSeatInDirOccupied
from advent import countOccupiedIn8
from advent import printGrid

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue(os.path.exists(os.path.join(os.path.dirname(__file__),"test_input.txt")))

    def test_inputFileLength(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input.txt"))
        self.assertEqual(len(struct),10)

    def test_processShortStruct(self):
        grid = processInputFile(os.path.join(os.path.dirname(__file__),"test_input2.txt"))
        self.assertEqual(len(grid),9)
        self.assertEqual( grid[4][3],1)
        
        self.assertEqual(8,countOccupiedIn8(grid,4,3))

    def test_processShortStruct2(self):
        grid = processInputFile(os.path.join(os.path.dirname(__file__),"test_input3.txt"))
        printGrid(grid)
        self.assertEqual(len(grid),3)
        self.assertEqual( grid[1][1], 1 )
        
        self.assertEqual(1,countOccupiedIn8(grid,1,0))

        #paths = processStruct(struct)
        #self.assertEqual( paths,8)

        


if __name__ == '__main__':
    unittest.main()