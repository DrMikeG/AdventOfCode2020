import unittest
import os

from advent import beginGame

class TestStringMethods(unittest.TestCase):

    def test_games(self):
        self.assertEqual(0,beginGame([0,3,6],10))
    def test_games2(self):        
        self.assertEqual(1,beginGame([1,3,2],2020))
    def test_games3(self):        
        self.assertEqual(10,beginGame([2,1,3],2020))
    def test_games4(self):        
        self.assertEqual(27,beginGame([1,2,3],2020))

    def test_gamesPuzzle(self):        
        self.assertEqual(492,beginGame([1,20,8,12,0,14],2020))

if __name__ == '__main__':
    unittest.main()