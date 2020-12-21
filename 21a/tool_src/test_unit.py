import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import intersectAllCombinations
from advent import hasUniqueIngredient
from advent import removeKnownAllergens
from advent import whichAllegensAreNotKnown
from advent import processInputFile2
class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadTestFile(self):
        filepath = os.path.join(os.path.dirname(__file__),"test_input_2.txt")
        struct = processInputFile(filepath)
        self.assertEqual(len(struct),3)
        self.assertTrue("dairy" in struct)
        self.assertTrue("soy" in struct)
        self.assertTrue("fish" in struct)
        self.assertEqual( len(struct["dairy"]),2 )
        dairy0 = struct["dairy"][0]
        self.assertEqual(len(dairy0) , 4)
        dairy1 = struct["dairy"][1]
        self.assertEqual(len(dairy1) , 4)
        self.assertEqual( len(struct["fish"]),2 )
        self.assertEqual( len(struct["soy"]),1 )

        self.assertEqual( ["mxmxvkd"], intersectAllCombinations(struct["dairy"]) )
        self.assertEqual( (True,"mxmxvkd"), hasUniqueIngredient("dairy",struct))
        self.assertEqual( (False,""), hasUniqueIngredient("fish",struct))
        self.assertEqual( (False,""), hasUniqueIngredient("soy",struct))
        
        known = removeKnownAllergens(struct)
        self.assertEqual( len(known), 3)

        allClear = []
        for key in struct:
            itemArrays = struct[key]
            for itemArray in itemArrays:
                for item in itemArray:
                    assert len(item) == 2
                    if item[1] == "":
                        allClear.append(item[0])

        allClearSet = set(allClear)
        print(allClearSet )
        print(len(allClearSet))

        processInputFile2(filepath,allClear)
    #def test_loadFile(self):
        #processInputFile(getInputPath())
    

if __name__ == '__main__':
    unittest.main()