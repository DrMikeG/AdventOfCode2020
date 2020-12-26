import os
import re
import copy
import math


def calcLoopSize(publicKey):
    subjectNumber = 7
    n = 1
    i = 0
    while True:
        n = (n * subjectNumber) % 20201227
        if n == publicKey:
            return i+1
        i += 1

def calcEncryptionKey(subjectNumber, loopSize):
    n = 1
    for i in range(loopSize):
        n = (n * subjectNumber) % 20201227
    return n


def mainTask():
    pass

if __name__ == "__main__":

    mainTask()
