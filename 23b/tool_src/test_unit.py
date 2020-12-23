import unittest
import os
from time import perf_counter
from advent import singleTurn
from advent import getNextupIndices
from advent import nextCurrentCupIndex
from advent import getAnswer
from advent import getDestinationCup
from advent import pickupCups
from advent import insertCupsAfterCup
class TestStringMethods(unittest.TestCase):

    def test_testRunReal1(self):
        t1_start = perf_counter()  
        cupCircle = [3,2,6,5,1,9,4,7,8]
        for n in range(10,1000001):
            cupCircle.append(n)
        self.assertEqual(len(cupCircle),1000000)
        
        currentCupIndex = 0
        for m in range(1):
            singleTurn(cupCircle,currentCupIndex,m+1)
            currentCupIndex = nextCurrentCupIndex(cupCircle,currentCupIndex)
        getAnswer(cupCircle)
        t1_stop = perf_counter() 
        print("Elapsed time for test test_testRunReal1 in seconds:",t1_stop-t1_start) 

    def test_testTestTun100000(self):
        t1_start = perf_counter()  
        cupCircle = [3,8,9,1,2,5,4,6,7]
        for n in range(10,1000001):
            cupCircle.append(n)
        self.assertEqual(len(cupCircle),1000000)
        
        currentCupIndex = 0
        for m in range(1000000):
            singleTurn(cupCircle,currentCupIndex,m+1)
            currentCupIndex = nextCurrentCupIndex(cupCircle,currentCupIndex)
        answer = getAnswer(cupCircle)
        self.assertEqual(len(answer),2)
        self.assertEqual(149245887792,answer[0]*answer[1])
        t1_stop = perf_counter() 
        print("Elapsed time for test test_testTestTun100000 in seconds:",t1_stop-t1_start) 


    def test_testRunReal100(self):
        cupCircle = [3,2,6,5,1,9,4,7,8]
        for n in range(10,1000001):
            cupCircle.append(n)
        self.assertEqual(len(cupCircle),1000000)
        currentCupIndex = 0
        for m in range(1):
            singleTurn(cupCircle,currentCupIndex,m+1)
            currentCupIndex = nextCurrentCupIndex(cupCircle,currentCupIndex)
        print(getAnswer(cupCircle))


if __name__ == '__main__':
    unittest.main()