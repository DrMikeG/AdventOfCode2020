import unittest
import os

from advent import singleTurn
from advent import getNextupIndices
from advent import nextCurrentCupIndex
from advent import getAnswer
from advent import getDestinationCup
from advent import pickupCups
from advent import insertCupsAfterCup
class TestStringMethods(unittest.TestCase):

    def test_testRound(self):
        #            0,1,2,3,4,5,6,7,8
        cupCircle = [3,8,9,1,2,5,4,6,7]
        #The crab picks up the three cups that are immediately clockwise of the current cup.
        
        self.assertEqual([1,2,3],getNextupIndices(cupCircle,0))
        
        self.assertEqual([7,8,0],getNextupIndices(cupCircle,6))

        self.assertEqual(2,getDestinationCup(cupCircle,0,[1,2,3]))

        addBack = pickupCups(cupCircle,[1,2,3])
        self.assertEqual([8,9,1],addBack)
        self.assertEqual([3,2,5,4,6,7],cupCircle)

        insertCupsAfterCup(cupCircle,2,addBack,0,3)
        self.assertEqual([3,2,8,9,1,5,4,6,7],cupCircle)

        currentCupIndex = 0
        currentCupIndex = nextCurrentCupIndex(cupCircle,currentCupIndex)
        self.assertEqual(1,currentCupIndex)

        cupCircle = [3,2,8,9,1,5,4,6,7]
        nextCupIndices = getNextupIndices(cupCircle,currentCupIndex)
        self.assertEqual([2,3,4],nextCupIndices)
        destinationCupLabel = getDestinationCup(cupCircle,currentCupIndex,nextCupIndices)
        self.assertEqual(7,destinationCupLabel)
        # There will be fewer things in cup
        addBack = pickupCups(cupCircle,nextCupIndices)
        self.assertEqual([8,9,1],addBack)
        insertCupsAfterCup(cupCircle,destinationCupLabel,addBack,1,2)
        self.assertEqual([3,2,5,4,6,7,8,9,1],cupCircle)

    def test_testRun10(self):
        cupCircle = [3,8,9,1,2,5,4,6,7]
        currentCupIndex = 0
        for m in range(10):
            singleTurn(cupCircle,currentCupIndex,m+1)
            currentCupIndex = nextCurrentCupIndex(cupCircle,currentCupIndex)
        self.assertEqual("92658374",getAnswer(cupCircle))

    def test_testRun100(self):
        cupCircle = [3,8,9,1,2,5,4,6,7]
        currentCupIndex = 0
        for m in range(100):
            singleTurn(cupCircle,currentCupIndex,m+1)
            currentCupIndex = nextCurrentCupIndex(cupCircle,currentCupIndex)
        self.assertEqual("67384529",getAnswer(cupCircle))

    def test_testRunReal100(self):
        cupCircle = [3,2,6,5,1,9,4,7,8]
        currentCupIndex = 0
        for m in range(100):
            singleTurn(cupCircle,currentCupIndex,m+1)
            currentCupIndex = nextCurrentCupIndex(cupCircle,currentCupIndex)
        self.assertEqual("25368479",getAnswer(cupCircle))


if __name__ == '__main__':
    unittest.main()