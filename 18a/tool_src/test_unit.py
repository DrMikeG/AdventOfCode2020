import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import firstFirstPairOfBrackets
from advent import sumWithoutBrackets
from advent import replaceFirstStringWithinBrackets
from advent import reduceStringToSingleValue

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadFile(self):
        processInputFile(getInputPath())
    
    def test_simpleSolveNoBrackets(self):
        self.assertEqual(7*5*6,sumWithoutBrackets("7 * 5 * 6"))
        self.assertEqual((((9 * 8) + 3) * 3) + 5,sumWithoutBrackets("9 * 8 + 3 * 3 + 5"))
        self.assertEqual(((6 + 3)* 9),sumWithoutBrackets("6 + 3 * 9"))
        #reduceStringToSingleValue("(7 * 5 * 6 + (9 * 8 + 3 * 3 + 5) + 7) * (6 + 3 * 9) + 6 + 7 + (7 * 5) * 4")

    def test_findBrackets(self):
        self.assertEqual( (13, 32), firstFirstPairOfBrackets("(7 * 5 * 6 + (9 * 8 + 3 * 3 + 5) + 7) * (6 + 3 * 9) + 6 + 7 + (7 * 5) * 4"))
        self.assertEqual("(7 * 5 * 6 + 230 + 7) * (6 + 3 * 9) + 6 + 7 + (7 * 5) * 4",replaceFirstStringWithinBrackets("(7 * 5 * 6 + (9 * 8 + 3 * 3 + 5) + 7) * (6 + 3 * 9) + 6 + 7 + (7 * 5) * 4") )
        self.assertEqual(71,reduceStringToSingleValue("1 + 2 * 3 + 4 * 5 + 6"))

    def test_solveTestData1(self):
        self.assertEqual(51,reduceStringToSingleValue("1 + (2 * 3) + (4 * (5 + 6))"))
    def test_solveTestData2(self):
        self.assertEqual(reduceStringToSingleValue("2 * 3 + (4 * 5)"),  26)
    def test_solveTestData3(self):
        self.assertEqual(reduceStringToSingleValue("5 + (8 * 3 + 9 + 3 * 4 * 3)"),  437)
    def test_solveTestData4(self):        
        self.assertEqual(reduceStringToSingleValue("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"),  12240)
    def test_solveTestData5(self):
        self.assertEqual(reduceStringToSingleValue("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"),  13632)


if __name__ == '__main__':
    unittest.main()