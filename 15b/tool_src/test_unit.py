import unittest
import os

from time import perf_counter
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
        t1_start = perf_counter()  
        self.assertEqual(63644,beginGame([1,20,8,12,0,14],30000000))
        t1_stop = perf_counter() 
        print("Elapsed time:", t1_stop, t1_start)  
        print("Elapsed time during the whole program in seconds:",t1_stop-t1_start) 

if __name__ == '__main__':
    unittest.main()