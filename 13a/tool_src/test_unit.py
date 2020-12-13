import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import processStruct
from advent import processLineOfInputIntoStruct

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_mainInputFileLength(self):
        struct = processInputFile( getInputPath() )
        self.assertEqual(len(struct),9)
        #print(list(struct))
        self.assertEqual(struct,[(0, 29), (18, 41), (9, 521), (7, 23), (4, 13), (3, 17), (13, 601), (5, 37), (12, 19)])

    def test_0(self):
        struct = []
        processLineOfInputIntoStruct("7,13,x,x,59,x,31,19",struct)
        self.assertEqual(struct,[(0, 7), (0, 13),(2, 59), (1,31),(0,19)])
        self.assertEqual(1068781,processStruct(1068780,struct))

    def test_1(self):
        struct = []
        processLineOfInputIntoStruct("17,x,13,19",struct)
        self.assertEqual(struct,[(0, 17), (1, 13), (0,19)])
        self.assertEqual(3417,processStruct(0,struct))
    
    def test_2(self):
        struct = []
        processLineOfInputIntoStruct("67,7,59,61",struct)
        self.assertEqual(754018,processStruct(0,struct))
    
    def test_3(self):
        struct = []
        processLineOfInputIntoStruct("67,x,7,59,61",struct)
        self.assertEqual(779210,processStruct(0,struct))
    
    def test_4(self):
        struct = []
        processLineOfInputIntoStruct("67,7,x,59,61",struct)
        self.assertEqual(1261476,processStruct(0,struct))
    
    def test_5(self):
        struct = []
        processLineOfInputIntoStruct("1789,37,47,1889",struct)
        self.assertEqual(1202161486,processStruct(0,struct))



if __name__ == '__main__':
    unittest.main()