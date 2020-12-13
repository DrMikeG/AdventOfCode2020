import os
import re
import copy
import math
import itertools


def processLineOfInputIntoStruct(line):
    # This very efficiently makes my pairs (0, 29), (19, 41), (29, 521), (37, 23), (42, 13), (46, 17), (60, 601), (66, 37), (79, 19)]
    raw = line.strip().split(',')
    buses = []
    for i, v in enumerate(raw):
        if v != 'x':
            buses.append((i, int(v)))
    return buses


def processInputFile(filePath):
    
    course = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            course = processLineOfInputIntoStruct(x)
        f.close()
    else :
        print("%s does not exist"%(filePath))

    return course

def lcm(a, b):
    # The least common multiple (L.C.M.) of two numbers is the smallest positive integer
    # that is perfectly divisible by the two given numbers.
    # For example, the L.C.M. of 12 and 14 is 84.

    # // operator to do integer division 
    return a * b // math.gcd(a, b)

def processStruct(buses):

    (time, step) = buses[0]

    for (delta, period) in buses[1:] :
            # itertools.count(start, [step])
            # start, start+step, start+2*step
        for time in itertools.count(time, step): # is multiple N of time also divisible by next number?
            if (time + delta) % period == 0:
                break
        

        step = lcm(step, period)

    print(time)

    return time

def getInputPath():
    return os.path.join(os.path.dirname(__file__),"input.txt")


def mainTask():
    input_path = getInputPath()
    struct = processInputFile(input_path)
    print("answer %d"%(processStruct(struct)))
    

if __name__ == "__main__":

    mainTask()