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

    def test_nPreviousNumbers(self):
        self.assertEqual( getNPreviousNumbers([1,2,3,4,5,6,7,8,9,10], 2, 2), [1,2] )
        self.assertEqual( getNPreviousNumbers([35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576], 5, 5), [35,20,15,25,47] )

    def test_nSumsFromPrevious(self):
        self.assertTrue( rangeHasPairTheSumToN([1,2],3) )
        self.assertTrue( rangeHasPairTheSumToN([5,0],5) )
        self.assertTrue( rangeHasPairTheSumToN([1,5,0],5) )
        self.assertTrue( rangeHasPairTheSumToN([0,5,1],6) )

        self.assertFalse( rangeHasPairTheSumToN([1,2],2) )
        self.assertFalse( rangeHasPairTheSumToN([4,4],2) )
        self.assertFalse( rangeHasPairTheSumToN([2,2],4) )
        
    def test_processShortStruct(self):
        struct = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
        preamble = 5
        stopAt = len(struct)
        subset = getRange(5,stopAt)
        # we want to process all the positions from 40 (first number with 5 before) up to 576
        self.assertEqual( struct[ subset[0] ],40) 
        self.assertEqual( struct[ subset[-1] ],576 )

        self.assertEqual( getNPreviousNumbers(struct,subset[0],preamble), [35,20,15,25,47] )

        self.assertEqual( 127, processStruct(struct,preamble) )

if __name__ == '__main__':
    unittest.main()