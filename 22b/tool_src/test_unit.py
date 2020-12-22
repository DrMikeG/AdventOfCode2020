import unittest
import os

from advent import playRound
from advent import playGame
from advent import calculateScore
class TestStringMethods(unittest.TestCase):

    
    #def test_testGameDoesNotGoOnForever(self):
    #    player1Dec = [43,19]
    #    player2Dec = [2,29,14]
    #    (winner,deckA,deckB) = playGame(player1Dec,player2Dec)
    #    self.assertEqual(0,winner)
    #    self.assertEqual([],deckA)

    #def test_testTestGame(self):
    #    player1Dec = [9, 2, 6, 3, 1]
    #    player2Dec = [5, 8, 4, 7, 10]
    #    (winner,deckA,deckB) = playGame(player1Dec,player2Dec)
    #    self.assertEqual(1,winner)
    #    self.assertEqual([7, 5, 6, 2, 4, 1, 10, 8, 9, 3],deckB)
    #    self.assertEqual(291,calculateScore(deckB))

    def test_playRealGame(self):
        player1Dec = [41,26,29,11,50,38,42,20,13, 9,40,43,10,24,35,30,23,15,31,48,27,44,16,12,14]
        player2Dec = [18, 6,32,37,25,21,33,28, 7, 8,45,46,49, 5,19, 2,39, 4,17, 3,22, 1,34,36,47]
        winningDeck = playGame(player1Dec,player2Dec)
        print(winningDeck)
        calculateScore(winningDeck)

if __name__ == '__main__':
    unittest.main()