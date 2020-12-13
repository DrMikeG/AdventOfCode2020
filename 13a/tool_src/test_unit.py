import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import processStruct
from advent import gcd

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_mainInputFileLength(self):
        struct = processInputFile( getInputPath() )
        self.assertEqual(len(struct),9)
        print(list(struct))
        self.assertEqual(struct,[(0, 29), (18, 41), (9, 521), (7, 23), (4, 13), (3, 17), (13, 601), (5, 37), (12, 19)])




if __name__ == '__main__':
    unittest.main()