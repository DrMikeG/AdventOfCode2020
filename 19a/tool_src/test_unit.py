import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import followEveryPath
from advent import testAllMessagesAndCountValid

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
        validMessages = followEveryPath(ruleStruct,0)
        self.assertEqual(True,  "ababbb" in validMessages)
        self.assertEqual(True,  "abbbab" in validMessages)
        self.assertEqual(False,  "aaabbb" in validMessages)
        self.assertEqual(False,  "bababa" in validMessages)
        self.assertEqual(False,  "aaaabbb" in validMessages)
        count = testAllMessagesAndCountValid(ruleStruct,messages)
        self.assertEqual(2,count)




        #stackObject= (0,0)
        #self.assertTrue(messageIsValid(messages[0],stackObject,ruleStruct))


if __name__ == '__main__':
    unittest.main()