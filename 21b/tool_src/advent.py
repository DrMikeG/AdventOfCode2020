import os
import re
import copy
import math

def parseLineOfInputToMapMultipleKeys(l,struct):
    # mxmxvkd kfcds sqjhc nhms (contains dairy, fish)\n
    twoParts = l.strip().split("(contains ",2)
    assert len(twoParts) == 2
    dirtyIngredients = twoParts[0].split(" ")
    cleandIngredients = []
    for dirty in dirtyIngredients:
        ing = dirty.strip()
        if ing != "":
            # pair ingredient with status
            cleandIngredients.append([ing,""])
    allStringNoBracket = twoParts[1].replace(")","")
    allergens = allStringNoBracket.split(",")
    assert len(allergens) > 0
    for allergen in allergens:
        cleanAllergen = allergen.strip()
        if not cleanAllergen in struct:
            struct[cleanAllergen] = []
        struct[cleanAllergen].append(cleandIngredients)

def intersectAllCombinations(combinations):
    setlist = []
    for listOfPairs in combinations:
        listOfFirsts = []
        for pair in listOfPairs:
            if pair[1] == "":
                listOfFirsts.append(pair[0])
        assert len(listOfFirsts) > 0
        setlist.append(set(listOfFirsts))
    u = set.intersection(*setlist)
    return list(u)

def hasUniqueIngredient(key,struct):
    assert key in struct
    combinations = struct[key]
    # intersect all the combinations - is there only on thing left? 
    remaining = intersectAllCombinations(combinations)
    assert len(remaining) > 0
    if len(remaining) == 1:
        return (True,remaining[0])
    else:
        return (False,"")

def markAllKnownAllergens(struct,known):
    for key in known:
        v = known[key]
        for k2 in struct:
            opts = struct[k2]
            for foodList in opts:
                for ingPairs in foodList:
                    assert len(ingPairs) == 2
                    if ingPairs[0] == v:
                        ingPairs[1] = key # this option is known to be an alergen - don't eat it

def removeKnownAllergens(struct):

    known = {}
    newKnown = True
    while newKnown:
        markAllKnownAllergens(struct,known)
        newKnown = False
        for key in struct:
            if key not in known:
                pair = hasUniqueIngredient(key,struct)
                if pair[0]:
                    newKnown = True
                    print("%s must contain %s"%(pair[1],key))
                    known[key] = pair[1]
    return known

def whichAllegensAreNotKnown(struct,known):
    notKnown = []
    
    for allengenKey in struct:
        if not allengenKey in known: 
            notKnown.append(allengenKey)
    return notKnown

def processLineOfInputIntoStruct(l,struct):
    parseLineOfInputToMapMultipleKeys(l,struct)

def processInputFile(filePath):
   
    struct = {}
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for l in f:
            processLineOfInputIntoStruct(l,struct)
        f.close()
    else :
        print("%s does not exist"%(filePath))
    
    return struct

def countTimePresentInLineOfInput(l,toCount):
    totalInLine = 0
    # mxmxvkd kfcds sqjhc nhms (contains dairy, fish)\n
    twoParts = l.strip().split("(contains ",2)
    assert len(twoParts) == 2
    dirtyIngredients = twoParts[0].split(" ")
    for dirty in dirtyIngredients:
        ing = dirty.strip()
        if ing in toCount:
            totalInLine = totalInLine + 1
    return totalInLine

def processInputFile2(filePath,toCount):
   
    total = 0
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for l in f:
            total = total + countTimePresentInLineOfInput(l,toCount)
        f.close()
    else :
        print("%s does not exist"%(filePath))
    
    print("total : %d"%(total))
    return total


def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    known = removeKnownAllergens(struct)
    print(known)
    """
    gpgrb must contain dairy
tjlz must contain eggs
gtjmd must contain fish
spbxz must contain nuts
pfdkkzp must contain peanuts
xcfpc must contain shellfish
txzv must contain soy
znqbr must contain wheat

gpgrb,tjlz,gtjmd,spbxz,pfdkkzp,xcfpc,txzv,znqbr,
"""
    
if __name__ == "__main__":

    mainTask()