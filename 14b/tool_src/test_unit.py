import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import processStruct
from advent import getAddressForFloating

from advent import toBinary
from advent import toInt

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_testInputFile2(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_2.txt") )
        self.assertEqual( len(struct), 4 )
        self.assertEqual(208,processStruct(struct))
        

    def test_roundTrip(self):
        for i in range(10000)[::17]:
            self.assertEqual(i,toInt(toBinary(i)))

    def test_mainInputFileLength(self):
        struct = processInputFile( getInputPath() )

    def test_getAddressForFloating(self):
        self.assertEqual([26,27,58,59],getAddressForFloating("000000000000000000000000000000X1001X",42))

    def test_getAddressForFloating2(self):
        self.assertEqual([16,17,18,19,24,25,26,27],getAddressForFloating("00000000000000000000000000000000X0XX",26))



if __name__ == '__main__':
    unittest.main()