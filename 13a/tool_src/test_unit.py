import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import nextBusLeavesIn
from advent import processStruct

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_mainInputFileLength(self):
        struct = processInputFile( getInputPath() )
        self.assertEqual(len(struct),10)
        self.assertEqual(struct[0],1002461)

    def test_testInputFileLength(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_2.txt"))
        self.assertEqual(len(struct),6)
        self.assertEqual(295, processStruct(struct))


if __name__ == '__main__':
    unittest.main()