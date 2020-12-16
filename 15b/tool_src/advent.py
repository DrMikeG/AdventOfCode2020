import os
import re
import copy
import math


def age(n,turn,lastspoken):
    if n not in lastspoken:
        return 0
    if n  in lastspoken and len(lastspoken[n]) == 1:
        return 0
    return lastspoken[n][-1] -lastspoken[n][-2]

def numberIsSpoken(n,turn,lastspoken):
    #if (turn % 100) == 0:
        #print("Turn %d number %d"%(turn,n))
    if n not in lastspoken:
        lastspoken[n] = [turn]
    else:
        lastspoken[n].append(turn)
        if len(lastspoken[n]) > 2:
            lastspoken[n].pop(0)

def beginGame(startingNumbers,runTo = 2020):
    lastspoken = {}
    turn = 1

    numberOnLastTurn = 0
    for n in startingNumbers:
        numberOnLastTurn =  n
        numberIsSpoken(n,turn,lastspoken)
        turn = turn + 1
    
    while (turn <= runTo):
        nAge = age(numberOnLastTurn,turn,lastspoken)
        numberIsSpoken(nAge,turn,lastspoken)
        numberOnLastTurn = nAge

        turn = turn + 1
    return numberOnLastTurn

def mainTask():

    answer = beginGame([1,20,8,12,0,14])

    print("answer %d"%(answer))


if __name__ == "__main__":

    mainTask()