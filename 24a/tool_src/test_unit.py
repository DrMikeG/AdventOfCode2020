import unittest
import os

from advent import convertLineDirectionToGridPosition
from advent import processInputFile

class TestStringMethods(unittest.TestCase):

    def test_simpleLines(self):
        
        tile = convertLineDirectionToGridPosition("se")
        self.assertEqual((0,1),tile)
        #esew flips a tile immediately adjacent to the reference tile,        
        tile = convertLineDirectionToGridPosition("esew")
        self.assertEqual((0,1),tile)
        tile = convertLineDirectionToGridPosition("ew")
        self.assertEqual((0,0),tile)
        #  and a line like nwwswee flips the reference tile itself.
        tile = convertLineDirectionToGridPosition("nwwswee")
        self.assertEqual((0,0),tile)


    def test_testFile(self):
        input_path = os.path.join(os.path.dirname(__file__),"test_input.txt")
        count = processInputFile(input_path)
        self.assertEqual(10,count)

if __name__ == '__main__':
    unittest.main()