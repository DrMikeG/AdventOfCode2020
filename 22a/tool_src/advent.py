import os
import re
import copy
import math


def singleTurn(playerADeck,playerBDeck):
    playerACard = playerADeck.pop(0)
    playerBCard = playerBDeck.pop(0)

    if playerACard > playerBCard:
        print("Player A wins %d > %d"%(playerACard,playerBCard))
        playerADeck.append(playerACard)
        playerADeck.append(playerBCard)
    elif playerBCard > playerACard:
        print("Player B wins %d > %d"%(playerBCard,playerACard))
        playerBDeck.append(playerBCard)
        playerBDeck.append(playerACard)

def playGame(playerADeck,playerBDeck):
    while len(playerADeck) > 0 and len(playerBDeck) > 0:
        singleTurn(playerADeck,playerBDeck)
    
    if len(playerADeck) == 0:
        print("playerB won!")
        return playerBDeck
    elif len(playerBDeck) == 0:
        print("playerA won!")
        return playerADeck
    assert False

def calculateScore(winningDeck):

    l = len(winningDeck)
    multi = 1
    score = 0
    for i in range(l,0,-1):
        val = winningDeck[i-1] *multi
        print("%d * %d = %d"%(winningDeck[i-1],multi,val))
        multi = multi + 1
        score = score + val
    print("score = %d"%(score))
    return score

def mainTask():
    return True
if __name__ == "__main__":

    mainTask()