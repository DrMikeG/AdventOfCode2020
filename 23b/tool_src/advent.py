import os
import re
import copy
import math


def getAnswer(cupCircle):
    # after the cup labeled 1, collect the other cups' labels clockwise into a single string with no extra characters; each number except 1 should appear exactly once.
    answer = []
    startAfter = cupCircle.index(1)
    n = len(cupCircle)
    if startAfter == (n-1): # final value
        answer.append(cupCircle[0])
        answer.append(cupCircle[1])
    elif startAfter == (n-2): # final value
        answer.append(cupCircle[n-1])
        answer.append(cupCircle[0])
    else:
        answer.append(cupCircle[startAfter+1])
        answer.append(cupCircle[startAfter+2])
    ##print(answer)
    ##print(cupCircle)
    return answer

def nextCurrentCupIndex(cupCircle,currentCupIndex):
    loopAt = len(cupCircle)
    return (currentCupIndex + 1) % loopAt

def getNextupIndices(cupCircle,currentCupIndex):
    #The crab picks up the three cups that are immediately clockwise of the current cup.
    loopAt = len(cupCircle)
    nextCupIndices = []
    printpick = []
    for i in range(currentCupIndex+1,currentCupIndex+4):
        nextCupIndices.append( i % loopAt )
        printpick.append(cupCircle[i % loopAt])
    #print("pick up: %s"%(list(printpick)))
    
    return nextCupIndices

def getDestinationCup(cupCircle,currentCupIndex,nextCupIndices):
    #The crab selects a destination cup: 
    # the cup with a label equal to the current cup's label minus one. 
    currentCupLabel = cupCircle[currentCupIndex]
    destinationCupLabel = currentCupLabel - 1

    highestLabel = max(cupCircle)
    lowestLabel = min(cupCircle)
    #assert(highestLabel == 9)
   
    if destinationCupLabel < lowestLabel:
        destinationCupLabel = highestLabel

   
    nextCupLabels = []
    for n in nextCupIndices:
        nextCupLabels.append(cupCircle[n])
    # If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up.
    # If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
    while destinationCupLabel in nextCupLabels:
        destinationCupLabel = destinationCupLabel - 1
        if destinationCupLabel < lowestLabel:
            destinationCupLabel = highestLabel
        assert destinationCupLabel in cupCircle
    
    #print("destination :%d"%(destinationCupLabel))

    assert destinationCupLabel in cupCircle
    assert not destinationCupLabel in nextCupLabels

    return destinationCupLabel


def pickupCups(cupCircle,nextCupIndices):
    toRemove = []
    for i in nextCupIndices:
        toRemove.append(cupCircle[i])
    for el in toRemove:
        cupCircle.remove(el)
    return toRemove

def insertCupsAfterCup(cupCircle,destinationCupLabel,addBack,currentCupIndex,currentCupLabel):

    # The crab places the cups it just picked up so that they are immediately clockwise of the destination cup.
    # They keep the same order as when they were picked up.
    assert destinationCupLabel in cupCircle
    startAt = cupCircle.index(destinationCupLabel) + 1
    for d in addBack[::-1]:
        cupCircle.insert(startAt,d)

    while cupCircle[currentCupIndex] != currentCupLabel:
        cupCircle.append(cupCircle.pop(0))

    assert cupCircle[currentCupIndex] == currentCupLabel

   # print("cups: %s\n"%(list(cupCircle)))

def singleTurn(cupCircle,currentCupIndex,move):
    
    #print("-- move %d --"%(move))
    #s = ""
    #for i in range(len(cupCircle)):
    #    if i == currentCupIndex:
    #        s = s + "("
    #    s = s + str(cupCircle[i])
     #   if i == currentCupIndex:
    #        s = s + ")"
    #    s = s + " "
    #print("cups: %s"%(s))

    currentCupLabel = cupCircle[currentCupIndex]

    nextCupIndices = getNextupIndices(cupCircle,currentCupIndex)#[1,2,3]

    destinationCupLabel = getDestinationCup(cupCircle,currentCupIndex,nextCupIndices)

    # There will be fewer things in cup
    addBack = pickupCups(cupCircle,nextCupIndices)

    insertCupsAfterCup(cupCircle,destinationCupLabel,addBack,currentCupIndex,currentCupLabel)



def mainTask():
    return True
if __name__ == "__main__":

    mainTask()