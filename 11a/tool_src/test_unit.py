import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import processStruct

class TestStringMethods(unittest.TestCase):

    def checkIfDuplicates(self,listOfElems):
        if len(listOfElems) == len(set(listOfElems)):
            return False
        else:
            return True

    def test_isFile(self):
        self.assertTrue(os.path.exists(getInputPath()))

    def test_inputFileLength(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(len(struct),90)
        self.assertFalse(self.checkIfDuplicates(struct))


    def test_processShortStruct(self):
        struct = [16,10,15,5,1,11,7,19,6,12,4]
        paths = processStruct(struct)
        self.assertEqual( paths,8)

    def test_processMedStruct(self):
        struct = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
        paths = processStruct(struct)
        self.assertEqual( paths,19208)
        


if __name__ == '__main__':
    unittest.main()