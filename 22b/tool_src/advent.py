import os
import re
import copy
import math


def subGame(playerACard,playerBCard,playerADeck,playerBDeck):
    # (For example, if player 1 draws the 3 card, and player 2 draws the 7 card, 
    # this would occur if player 1 has at least 3 cards left and player 2 has at least 7 cards left,
    # not counting the 3 and 7 cards that were drawn.)
    # To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck 
    # (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the 3 card, their deck in the sub-game would be copies of the next three cards in their deck.)
    playerASubGameDeck = []
    playerBSubGameDeck = []
    for a in range(playerACard):
        playerASubGameDeck.append(playerADeck[a])
    assert len(playerASubGameDeck) == playerACard
    for b in range(playerBCard):
        playerBSubGameDeck.append(playerBDeck[b])
    assert len(playerBSubGameDeck) == playerBCard

    (winner,aDeck,bDeck) = playGame(playerASubGameDeck,playerBSubGameDeck)
    return winner


def playRound(playerADeck,playerBDeck):
    playerACard = playerADeck.pop(0)
    playerBCard = playerBDeck.pop(0)

    print("Player 1 plays: %d"%playerACard)
    print("Player 2 plays: %d"%playerBCard)
    # If both players have at least as many cards remaining in their deck as the value of the card they just drew,
    # the winner of the round is determined by playing a new game of Recursive Combat (see below).
    remainingCardCountForPlayerA = len(playerADeck)
    remainingCardCountForPlayerB = len(playerBDeck)
    playerACanRecurse = remainingCardCountForPlayerA >= playerACard
    playerBCanRecurse = remainingCardCountForPlayerB >= playerBCard
    
    winner = 0

    if playerACanRecurse and playerBCanRecurse:
        print("Playing a sub-game to determine the winner...")
        winner = subGame(playerACard,playerBCard,playerADeck,playerBDeck)
    else:
        if playerACard > playerBCard:
            print("Player A wins %d > %d"%(playerACard,playerBCard))
            winner = 0
        elif playerBCard > playerACard:
            print("Player B wins %d > %d"%(playerBCard,playerACard))
            winner = 1


    # Otherwise, at least one player must not have enough cards left in their deck to recurse; 
    # the winner of the round is the player with the higher-value card.
    if winner == 0:
        playerADeck.append(playerACard)
        playerADeck.append(playerBCard)
        return 0
    elif winner == 1:
        playerBDeck.append(playerBCard)
        playerBDeck.append(playerACard)
        return 1

def playGame(playerADeck,playerBDeck):
    
    print("=== Game n ===")
    previousRounds = []
    round = 0
    while len(playerADeck) > 0 and len(playerBDeck) > 0:
        round = round + 1
        
        print("-- Round %d (Game n) --"%(round))
        print("Player 1's deck:",playerADeck)
        print("Player 2's deck:",playerBDeck)
    
        if (playerADeck,playerBDeck) in previousRounds:
            print(" ** Player 1 wins to prevent infinite game! **")
            return (0,[],[]) # player A one, ignore decks
        # Before either player deals a card, 
        # if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks,
        # the game instantly ends in a win for player 1.
        # Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
        previousRounds.append((playerADeck.copy(),playerBDeck.copy()))

        winner = playRound(playerADeck,playerBDeck)

        if winner == 0:
            print("Player 1 wins round %d"%(round))
        elif winner == 1:
            print("Player 2 wins round %d"%(round))
    
    if len(playerADeck) == 0:
        print("player2 won game")
        return (1,playerADeck,playerBDeck)
    elif len(playerBDeck) == 0:
        print("player1 won game")
        return (0,playerADeck,playerBDeck)
    
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