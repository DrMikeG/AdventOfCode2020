import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import testIsMessagesValid
from advent import testAllMessagesAndCountValid
from advent import canIMatchThisStringForThisRule
class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadTestFile(self):
        ruleStruct, messages = processInputFile( os.path.join(os.path.dirname(__file__),"test_input_2.txt") )
        self.assertEqual(6,len(ruleStruct))
        self.assertEqual(5,len(messages))
        self.assertEqual(ruleStruct[4],[[-1]]) #4: "a" only one option, 'a'
        self.assertEqual(ruleStruct[5],[[-2]]) #5: "b" only one option, 'b'
        self.assertEqual(ruleStruct[2],[[4,4],[5,5]])# 2: 4 4 | 5 5
        self.assertEqual(messages[0],"ababbb")
        self.assertEqual(True, canIMatchThisStringForThisRule("ba",3,{},ruleStruct))
        self.assertEqual(True, canIMatchThisStringForThisRule("bb",2,{},ruleStruct))
        self.assertEqual(True, canIMatchThisStringForThisRule("babb",1,{},ruleStruct))
        self.assertEqual(True, canIMatchThisStringForThisRule("a",4,{},ruleStruct))
        self.assertEqual(True, canIMatchThisStringForThisRule("b",5,{},ruleStruct))
        self.assertEqual(True, testIsMessagesValid(ruleStruct,"ababbb"))
        self.assertEqual(True,  testIsMessagesValid(ruleStruct,"abbbab"))
        self.assertEqual(False,  testIsMessagesValid(ruleStruct,"aaabbb"))
        self.assertEqual(False,  testIsMessagesValid(ruleStruct,"bababa"))
        self.assertEqual(False,  testIsMessagesValid(ruleStruct,"aaaabbb"))
        count = testAllMessagesAndCountValid(ruleStruct,messages)
        self.assertEqual(2,count)

    def test_loadRealFile(self):
        ruleStruct, messages = processInputFile( getInputPath()  )
        self.assertEqual(130,len(ruleStruct))
        self.assertEqual(459,len(messages))
        self.assertEqual(True, canIMatchThisStringForThisRule("b",12,{},ruleStruct))
        self.assertEqual(True, canIMatchThisStringForThisRule("a",106,{},ruleStruct))
        self.assertEqual(True, canIMatchThisStringForThisRule("ababbbababaaaaabbbabaaaa",0,{},ruleStruct))
        self.assertEqual(True, canIMatchThisStringForThisRule("abaaabaaabaaaaaaaabbaaab",0,{},ruleStruct))
        #self.assertEqual(True, canIMatchThisStringForThisRule("abbbbbaabbabbabababaaabaaabbaabb",0,{},ruleStruct))
        #self.assertEqual(True, canIMatchThisStringForThisRule("bbbaabaaababbaabbbabbbbbaabbabab",0,{},ruleStruct))




if __name__ == '__main__':
    unittest.main()