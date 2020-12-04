import os
import re

def isCharacterN(stringValue,characterIndex,wantedChar):
    return stringValue[characterIndex] == wantedChar

def processLineOfInputIntoStruct(line,struct):
    struct.append(line)

def processInputFile(filePath):
    
    struct = []
    if os.path.exists(filePath):
        with open(filePath) as f:
            lines = f.read()
        struct = lines.split("\n\n")
    else :
        print("%s does not exist"%(filePath))
    return struct

def isValidByr(byr):
    # four digits; at least 1920 and at most 2002.
    if (len(byr) < 4):
        return False
    intbyr = int(byr)
    return intbyr > 1919 and intbyr < 2003

def isValidIyr(iyr):
    # four digits; at least 2010 and at most 2020.
    if (len(iyr) < 4):
        return False
    intiyr = int(iyr)
    return intiyr > 2009 and intiyr < 2021

def isValidEyr(eyr):
    # four digits; at least 2020 and at most 2030.
    if (len(eyr) < 4):
        return False
    inteyr = int(eyr)
    return inteyr > 2019 and inteyr < 2031

def isValidHgt(hgt):
    # a number followed by either cm or in:
    if(hgt[-1] == 'n' and hgt[-2]=='i'):
        inches = int(hgt[:-2])
        return inches > 58 and inches < 77
    if(hgt[-1] == 'm' and hgt[-2]=='c'):
        cms = int(hgt[:-2])
        return cms > 149 and cms < 194
    return False

def isValidHcl(hcl):
    if (hcl[0] == '#' and len(hcl) == 7):
        test_str =hcl[1:]
        pattern = r'[^a-f0-9]'
        if re.search(pattern, test_str):
            #Character other then . a-z 0-9 was found
            return False
        else:
            #No character other then . a-z 0-9 was found
            return True
    return False

def isValidEcl(ecl):
    #amb blu brn gry grn hzl oth
    validList = ["amb","blu","brn","gry","grn","hzl","oth"]
    if (len(ecl) == 3):
        return ecl in validList
    return False

def isValidPid(pid):
    if (len(pid) == 9):
        pattern = r'[^0-9]'
        if re.search(pattern, pid):
            return False
        else:
            return True
    return False


def processStruct(struct):

    
    validValues = []
    numberOfPassports = len(struct)
    print("Number of numberOfPassports %d" %(numberOfPassports))

    for passport in struct :
        lines = re.split('[\n :]',passport)
        print(lines)

        a = b = c = d = e = f = g = False

        if ("byr" in lines):
            a = isValidByr(lines[lines.index("byr")+1])
        if ("iyr" in lines):
            b = isValidIyr(lines[lines.index("iyr")+1])
        if ("eyr" in lines):
            c = isValidEyr(lines[lines.index("eyr")+1])
        if ("hgt" in lines):
            d = isValidHgt(lines[lines.index("hgt")+1])
        if ("hcl" in lines):
            e = isValidHcl(lines[lines.index("hcl")+1])
        if ("ecl" in lines):
            f = isValidEcl(lines[lines.index("ecl")+1])
        if ("pid" in lines):
            g = isValidPid(lines[lines.index("pid")+1])

        #"cid"
        if a and b and c and d and e and f and g :
            validValues.append(passport)

    print(len(validValues))


def mainTask():
    input_path = os.path.join(os.path.dirname(__file__),"input.txt")
    struct = processInputFile(input_path)
    processStruct(struct)

if __name__ == "__main__":

    mainTask()