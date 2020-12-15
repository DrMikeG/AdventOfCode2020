import unittest
import os

from advent import beginGame

class TestStringMethods(unittest.TestCase):

    #def test_games(self):
    #    self.assertEqual(175594,beginGame([0,3,6],30000000))
    #def test_games2(self):        
    #    self.assertEqual(2578,beginGame([1,3,2],30000000))
    #def test_games3(self):        
    #    self.assertEqual(3544142,beginGame([2,1,3],30000000))
    #def test_games4(self):        
    #    self.assertEqual(261214,beginGame([1,2,3],30000000))

    def test_gamesPuzzle(self):        
        self.assertEqual(492,beginGame([1,20,8,12,0,14],30000000))

if __name__ == '__main__':
    unittest.main()