import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import processStruct
from advent import applyMaskBinary

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_masking(self):
        self.assertEqual(73,applyMaskBinary("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",11))
        self.assertEqual(101,applyMaskBinary("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",101))
        self.assertEqual(64,applyMaskBinary("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",0))

    def test_testInputFile2(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_2.txt") )
        self.assertEqual( len(struct), 4 )
        self.assertEqual( 165, processStruct(struct) )

    def test_mainInputFileLength(self):
        struct = processInputFile( getInputPath() )
        self.assertEqual(len(struct),554)


if __name__ == '__main__':
    unittest.main()