import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import firstFirstPairOfBrackets
from advent import sumWithoutBrackets
from advent import replaceFirstStringWithinBrackets
from advent import reduceStringToSingleValue
from advent import insertBracketsForAllAdditions

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadFile(self):
        #processInputFile(getInputPath())
        self.assertTrue(True)
    
    def test_Preprocess1(self):
        self.assertTrue(True)
        self.assertEqual(" ( 6 + 3 ) ",insertBracketsForAllAdditions("6 + 3"))

    def test_Preprocess2(self):
        self.assertTrue(True)
        self.assertEqual(" ( (6 + 3) ) ",insertBracketsForAllAdditions("(6 + 3)"))

    def test_Preprocess3(self):
        self.assertTrue(True)
        self.assertEqual("( ( 6 + 3 ) )",insertBracketsForAllAdditions("( 6 + 3 )"))

    def test_Preprocess4(self):
        self.assertTrue(True)
        self.assertEqual("( ( ( 4 + 6 ) + 3 ) )",insertBracketsForAllAdditions("( 4 + 6 + 3 )"))

    def test_Preprocess5(self):
        self.assertTrue(True)
        self.assertEqual(" ( 4 + 6 ) * ( ( 2 + 3 ) )",insertBracketsForAllAdditions("4 + 6 * ( 2 + 3 )"))

    def test_Preprocess7(self):
        self.assertTrue(True)
        self.assertEqual("8 * ( ( 3 + 9 ) + 3 ) ",insertBracketsForAllAdditions("8 * 3 + 9 + 3"))

    def test_Preprocess6(self):
        self.assertTrue(True)
        self.assertEqual(51,reduceStringToSingleValue(insertBracketsForAllAdditions("1 + (2 * 3) + (4 * (5 + 6))")))
        self.assertEqual(46,reduceStringToSingleValue(insertBracketsForAllAdditions("2 * 3 + (4 * 5)")))
        self.assertEqual(1445,reduceStringToSingleValue(insertBracketsForAllAdditions("5 + (8 * 3 + 9 + 3 * 4 * 3)")))
        self.assertEqual(669060,reduceStringToSingleValue(insertBracketsForAllAdditions("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")))
        self.assertEqual(23340,reduceStringToSingleValue(insertBracketsForAllAdditions("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")))

    def test_Preprocess8(self):
        self.assertEqual(" ( ( ( ( (8 + (8 * 4 )) + (7 + 3 * 5) ) + 4 ) + 4 ) + 7 )",insertBracketsForAllAdditions("(8 + (8 * 4)) + (7 + 3 * 5) + 4 + 4 + 7"))



if __name__ == '__main__':
    unittest.main()