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
        self.assertEqual(struct,[(0, 29), (19, 41), (29, 521), (37, 23), (42, 13), (46, 17), (60, 601), (66, 37), (79, 19)])

    def test_0(self):
        struct = []
        struct = processLineOfInputIntoStruct("7,13,x,x,59,x,31,19")
        self.assertEqual(struct,[(0, 7), (1, 13),(4, 59), (6,31),(7,19)])
        self.assertEqual(1068781,processStruct(struct))

    def test_1(self):
        struct = []
        struct = processLineOfInputIntoStruct("17,x,13,19")
        self.assertEqual(struct,[(0, 17), (2, 13), (3,19)])
        self.assertEqual(3417,processStruct(struct))

        # (0, 17), (2, 13), (3,19)]
        # for each n:
        #   is (17*n)+2 divisible by 13?
        
        # (17*6)+2 = 104 / 13 = 8
        # lcm(17,13) = 221 (17*13)
        # every 221 steps from 102, bus 0 and 1 will be in sync
        # now lets consider bus 3
        # 102+(15*221) = 3417
        # ( 3417 + 3 ) / 19 = 180


    
    def test_2(self):
        struct = []
        struct = processLineOfInputIntoStruct("67,7,59,61")
        self.assertEqual(754018,processStruct(struct))
    
    def test_3(self):
        struct = []
        struct = processLineOfInputIntoStruct("67,x,7,59,61")
        self.assertEqual(779210,processStruct(struct))
    
    def test_4(self):
        struct = []
        struct = processLineOfInputIntoStruct("67,7,x,59,61")
        self.assertEqual(1261476,processStruct(struct))
    
    def test_5(self):
        struct = []
        struct = processLineOfInputIntoStruct("1789,37,47,1889")
        self.assertEqual(1202161486,processStruct(struct))

if __name__ == '__main__':
    unittest.main()