# Solution from https://github.com/ajurna/aoc2020/blob/main/day23/23.py

from dataclasses import dataclass, field

@dataclass
class Cup:
    value: int
    next_cup: "Cup" = field(repr=False)

    def __init__(self, val, next_cup=None):
        self.value = int(val)
        self.next_cup = next_cup

def playNRounds(first_cup, cups, rotations):
    max_key = max(cups.keys())
    cup = first_cup
    for _ in range(rotations):
        # Cups to move: cup,[a,b,c]
        a = cup.next_cup
        c = a.next_cup.next_cup
        dest = cup.value - 1
        while True:
            # if destination is already in a,b,c
            if dest in [a.value, a.next_cup.value, c.value]:
                pass # progress to dest -=
            elif dest < 0: # loop back to max value
                dest = max_key
                continue
            elif dest in cups:
                dest_cup = cups[dest]
                break
            dest -= 1 # since when was there a -=?

        # insert a,b,c after break_cup
        break_cup = dest_cup.next_cup
        cup.next_cup = c.next_cup
        dest_cup.next_cup = a
        c.next_cup = break_cup
        cup = cup.next_cup

    return cups

data = list('326519478')
cups = {}

last_cup = Cup(data.pop(0))
first_cup = last_cup
# create cup for first value in data and start making cup list
cups[last_cup.value] = last_cup
# define linked list for all remaining values in data
# final cup has no forward link
for c in data:
    cup = Cup(c)
    last_cup.next_cup = cup
    cups[cup.value] = cup
    last_cup = cup
# add to linked list for remaning million cups
for c in range(max(cups.keys())+1, 1000001):
    cup = Cup(c)
    last_cup.next_cup = cup
    cups[cup.value] = cup
    last_cup = cup
# make into circular linked list by joining end of list to start
last_cup.next_cup = first_cup

# play n rounds
cups = playNRounds(first_cup, cups, 10000000)
# cup after cup[1]
cup1 = cups[1].next_cup
# cup after cup[2]
cup2 = cup1.next_cup
print("Part 2:", cup1.value * cup2.value)