import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import rowIndexAfter
from advent import parseTicketFromRowString
from advent import parseFieldRuleFromRow
from advent import isNumberValidForRule
from advent import findTicketValuesThatAreNotValid
from advent import parseInputFile
from advent import sumAllBadTicketValues
from advent import removeAllBadTickets
from advent import eliminate
from advent import processOfElimination

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadFile(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(260,len(struct))

    def test_findYourTicket(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(20,rowIndexAfter(struct,"your ticket"))
        self.assertEqual([131,103,109,67,127,97,89,79,163,59,73,83,61,107,53,193,167,101,71,197],parseTicketFromRowString(struct[21]))

    def test_finNearbyTickets(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(22,rowIndexAfter(struct,"nearby tickets"))
    
    def test_parseRule(self):
        struct = processInputFile(getInputPath())
        rule = parseFieldRuleFromRow(struct,0)
        self.assertEqual(len(rule),5)
        self.assertEqual(rule[1],37)
        self.assertEqual(rule[2],594)
        self.assertEqual(rule[3],615)
        self.assertEqual(rule[4],952)
        self.assertEqual(False, isNumberValidForRule(rule,36))
        self.assertEqual(True, isNumberValidForRule(rule,37))
        self.assertEqual(True, isNumberValidForRule(rule,500))
        self.assertEqual(False, isNumberValidForRule(rule,600))
        self.assertEqual(True, isNumberValidForRule(rule,615))
        self.assertEqual(True, isNumberValidForRule(rule,800))
        self.assertEqual(True, isNumberValidForRule(rule,952))
        self.assertEqual(False, isNumberValidForRule(rule,1000))

    def test_loadShortFile(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_2.txt"))
        self.assertEqual(10,len(struct))
        rules, myTicket, otherTickets = parseInputFile(struct)
        self.assertEqual(3,len(rules))
        self.assertEqual([7,1,14],myTicket)
        self.assertEqual([[7,3,47],[40,4,50],[55,2,20],[38,6,12]],otherTickets)
        sum = sumAllBadTicketValues(rules, myTicket, otherTickets)
        self.assertEqual(71,sum)
        goodTickets = removeAllBadTickets(rules, myTicket, otherTickets)
        self.assertEqual(1,len(goodTickets))
        possibles = eliminate(rules,myTicket,otherTickets)
        processOfElimination(possibles)


if __name__ == '__main__':
    unittest.main()