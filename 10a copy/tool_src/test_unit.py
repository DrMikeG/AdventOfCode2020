import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import processStruct

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue(os.path.exists(getInputPath()))

    def test_inputFileLength(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(len(struct),90)

    def test_processShortStruct(self):
        struct = [16,10,15,5,1,11,7,19,6,12,4]
        dist = processStruct(struct)
        self.assertEqual( dist[1],7)
        self.assertEqual( dist[3],5)

    def test_processMedStruct(self):
        struct = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
        dist = processStruct(struct)
        self.assertEqual( dist[1],22)
        self.assertEqual( dist[3],10)


if __name__ == '__main__':
    unittest.main()