import unittest
import os

from advent import singleTurn
from advent import playGame
from advent import calculateScore
class TestStringMethods(unittest.TestCase):

    def test_testRound(self):
        player1Dec = [9,2,6,3,1]
        player2Dec = [5,8,4,7,10]
        singleTurn(player1Dec,player2Dec)
        self.assertEqual([2, 6, 3, 1, 9, 5],player1Dec)
        self.assertEqual([8, 4, 7, 10],player2Dec)

    def test_testGame(self):
        player1Dec = [9,2,6,3,1]
        player2Dec = [5,8,4,7,10]
        winningDeck = playGame(player1Dec,player2Dec)
        self.assertEqual([3, 2, 10, 6, 8, 5, 9, 4, 7, 1],winningDeck)
        self.assertEqual(306,calculateScore(winningDeck))

    def test_playRealGame(self):
        player1Dec = [41,26,29,11,50,38,42,20,13, 9,40,43,10,24,35,30,23,15,31,48,27,44,16,12,14]
        player2Dec = [18, 6,32,37,25,21,33,28, 7, 8,45,46,49, 5,19, 2,39, 4,17, 3,22, 1,34,36,47]
        winningDeck = playGame(player1Dec,player2Dec)
        print(winningDeck)
        calculateScore(winningDeck)

if __name__ == '__main__':
    unittest.main()