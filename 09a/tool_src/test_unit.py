import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import getNPreviousNumbers
from advent import rangeHasPairTheSumToN
from advent import processStruct
from advent import getRange

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue(os.path.exists(getInputPath()))

    def test_inputFileLength(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(len(struct),1000)

 
        
    def test_processShortStruct(self):
        struct = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
        target = 127
        self.assertEqual( 62, processStruct(struct,target) )

if __name__ == '__main__':
    unittest.main()