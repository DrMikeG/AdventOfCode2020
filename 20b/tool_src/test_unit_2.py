import unittest
import os

from advent2 import getInputPath
from advent2 import processInputFile
from advent2 import seaMonsters
from advent2 import ifSeaMonsterMarkPositions
from advent2 import writeImageToFile
from advent2 import countHashes
from advent2 import rotate90
from advent2 import flipNorthToSouth
class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_loadRealFile(self):
        image = processInputFile( os.path.join(os.path.dirname(__file__),"output.txt") )
        monsters = seaMonsters()
        for _ in range(4):
            for r in range(120):
                for c in range(120):
                    ifSeaMonsterMarkPositions(image,r,c,monsters[0])
            image = rotate90(image)
        
        image = flipNorthToSouth(image)
        for _ in range(4):
            for r in range(120):
                for c in range(120):
                    ifSeaMonsterMarkPositions(image,r,c,monsters[0])
            image = rotate90(image)

        print(countHashes(image))

        writeImageToFile(image)


if __name__ == '__main__':
    unittest.main()