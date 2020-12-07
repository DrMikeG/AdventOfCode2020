import unittest
import os

from advent import isCharacterN
from advent import getInputPath
from advent import processInputFile
from advent import splitBagContain
from advent import parseContentRule
from advent import parseRuleTitle
from advent import followPathLookingFor
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_isCharacterN(self):
        self.assertTrue(isCharacterN("FBFBBFBLRR",0,"F"))

    def test_isFile(self):
        self.assertTrue(os.path.exists(getInputPath()))

    def test_inputFileLength(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(len(struct),594)



    # split at 'bags contain' (each line should contain this)
    # split comma separated list ending with . (each line should contain this)
    # remove bag or bags
    # start with number
    # colour description contains exactly 1 space
    def test_inputLinesContainBagString(self):
        if os.path.exists(getInputPath()):
            f = open(getInputPath(), "r")
            for x in f:
                self.assertTrue("bags contain" in x)
                newStringParts = splitBagContain(x)
                ruleTitle = parseRuleTitle(newStringParts[0])
                rules = map(parseContentRule,newStringParts[1:])
                #print(ruleTitle,list(rules))
                #print(newStringParts)
                # first token is "A B"

            f.close()

    def test_trickyInputLine01(self):
        trickyLine = 'pale purple bags contain no other bags.'
        newStringParts = splitBagContain(trickyLine)
        ruleTitle = parseRuleTitle(newStringParts[0])
        rules = map(parseContentRule,newStringParts[1:])
        #print(ruleTitle,list(rules))

    def test_parseContentRule01(self):
        self.assertEqual((3,'vibrant','gray'),parseContentRule(' 3 vibrant gray bags'))
        self.assertEqual((1,'pale','teal'),parseContentRule(' 1 pale teal bag.\n'))

    def test_parseContentRuleTitle(self):
        self.assertEqual(('drab','crimson'),parseRuleTitle('drab crimson '))
        self.assertEqual(('plaid','bronze'),parseRuleTitle('plaid bronze '))

    def test_followPathLookingFor_01(self):
        struct = {}
        struct[('shiny','gold')]= [(2,'dark','red')]
        struct[('dark' ,'red')]= [(2,'dark','orange')]
        struct[('dark' ,'orange')]= [(2,'dark','yellow')]
        struct[('dark' ,'yellow')]= [(2,'dark','green')]
        struct[('dark' ,'green')]= [(2,'dark','blue')]
        struct[('dark' ,'blue')]= [(2,'dark','violet')]
        struct[('dark' ,'violet')]= [(0,'','')]
        stack = [('shiny','gold')]
        bagCount = -1
        followPathLookingFor(struct,stack,'',bagCount)
        print(bagCount)
        self.assertEqual(126,bagCount)


if __name__ == '__main__':
    unittest.main()