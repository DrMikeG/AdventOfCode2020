import unittest
import os

from advent2 import getInputPath
from advent2 import processInputFile
from advent2 import seaMonsters
from advent2 import ifSeaMonsterMarkPositions
from advent2 import writeImageToFile

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadTestFile2(self):
        image = processInputFile( os.path.join(os.path.dirname(__file__),"test_output_2.txt") )
        self.assertEqual(len(image),3)
        self.assertEqual(len(image[0]),20)
        monsters = seaMonsters()
        self.assertEqual(len(monsters),8)
        for monster in monsters:
            h = len(monster)
            w = len(monster[0])
            self.assertTrue( (h == 3 and w == 20) or (w == 3 and h == 20))

        for r in range(1):
            for c in range(1):
                ifSeaMonsterMarkPositions(image,r,c,monsters[0])
        #writeImageToFile(image)

    def test_loadTestFile(self):
        image = processInputFile( os.path.join(os.path.dirname(__file__),"test_output.txt") )
        self.assertEqual(len(image),24)
        self.assertEqual(len(image[0]),24)
        monsters = seaMonsters()
        self.assertEqual(len(monsters),8)
        for r in range(-20,24+20):
            for c in range(-20,24+20):
                ifSeaMonsterMarkPositions(image,r,c,monsters[0])
        writeImageToFile(image)


if __name__ == '__main__':
    unittest.main()