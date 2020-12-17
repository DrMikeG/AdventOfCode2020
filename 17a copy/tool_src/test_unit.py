import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import isCellActive
from advent import getBoundingBox
from advent import countActive
from advent import doCycles
from advent import printBoundingBox


class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadFile(self):
        processInputFile(getInputPath())
        # row 0 .###.#.#
        self.assertEqual(False, isCellActive(0,0,0) )
        self.assertEqual(True, isCellActive(1,0,0) )
        self.assertEqual(True, isCellActive(2,0,0) )
        self.assertEqual(True, isCellActive(3,0,0) )
        self.assertEqual(False, isCellActive(4,0,0) )
        self.assertEqual(True, isCellActive(5,0,0) )
        self.assertEqual(False, isCellActive(6,0,0) )
        self.assertEqual(True, isCellActive(7,0,0) )
        # row 5 ########
        self.assertEqual(True, isCellActive(0,5,0) )
        self.assertEqual(True, isCellActive(1,5,0) )
        self.assertEqual(True, isCellActive(2,5,0) )
        self.assertEqual(True, isCellActive(3,5,0) )
        self.assertEqual(True, isCellActive(4,5,0) )
        self.assertEqual(True, isCellActive(5,5,0) )
        self.assertEqual(True, isCellActive(6,5,0) )
        self.assertEqual(True, isCellActive(7,5,0) )

        self.assertEqual((0,0,0,7,7,0),getBoundingBox())

        self.assertEqual(41,countActive())

    def test_loadTestFile(self):
        processInputFile(os.path.join(os.path.dirname(__file__),"test_input_2.txt"))
        self.assertEqual(False, isCellActive(0,0,0) )
        self.assertEqual(True, isCellActive(1,0,0) )
        self.assertEqual(False, isCellActive(2,0,0) )
        
        self.assertEqual((0,0,0,2,2,0),getBoundingBox())
        printBoundingBox()
        
        doCycles(1)
        self.assertEqual((0,0,-1,2,2,1),getBoundingBox())
        printBoundingBox()


        
        # After 1 cycle:
        # z=-1
        # #..
        # ..#
        # .#.
        z = -1
        self.assertEqual(True, isCellActive(0,0,z) )
        self.assertEqual(False,  isCellActive(1,0,z) )
        self.assertEqual(False, isCellActive(2,0,z) )
        self.assertEqual(False, isCellActive(0,1,z) )
        self.assertEqual(False,  isCellActive(1,1,z) )
        self.assertEqual(True, isCellActive(2,1,z) )
        self.assertEqual(False, isCellActive(0,2,z) )
        self.assertEqual(True,  isCellActive(1,2,z) )
        self.assertEqual(False, isCellActive(2,2,z) )
        # z=0
        # #.#
        # .##
        # .#.
        z = 0
        self.assertEqual(True, isCellActive(0,0,z) )
        self.assertEqual(False,  isCellActive(1,0,z) )
        self.assertEqual(True, isCellActive(2,0,z) )
        self.assertEqual(False, isCellActive(0,1,z) )
        self.assertEqual(True,  isCellActive(1,1,z) )
        self.assertEqual(True, isCellActive(2,1,z) )
        self.assertEqual(True, isCellActive(0,2,z) )
        self.assertEqual(False,  isCellActive(1,2,z) )
        self.assertEqual(True, isCellActive(2,2,z) )
        z = +1
        # z=1
        # #..
        # ..#
        # .#.

        self.assertEqual(True, isCellActive(0,0,z) )
        self.assertEqual(False,  isCellActive(1,0,z) )
        self.assertEqual(False, isCellActive(2,0,z) )
        self.assertEqual(False, isCellActive(0,1,z) )
        self.assertEqual(False,  isCellActive(1,1,z) )
        self.assertEqual(True, isCellActive(2,1,z) )
        self.assertEqual(False, isCellActive(0,2,z) )
        self.assertEqual(True,  isCellActive(1,2,z) )
        self.assertEqual(False, isCellActive(2,2,z) )

       
        doCycles(5)
        self.assertEqual(112,countActive())


if __name__ == '__main__':
    unittest.main()