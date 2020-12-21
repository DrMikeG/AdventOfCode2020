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
    
    """
    def test_loadATestFile(self):
        image = processInputFile( os.path.join(os.path.dirname(__file__),"test_without_borders.txt") )
        monsters = seaMonsters()
        print(monsters[0])

        for i in range(4):
            print("orientation %d"%(i))
            for r in range(-20,140):
                for c in range(-20,140):
                    ifSeaMonsterMarkPositions(image,r,c,monsters[0])
            image = rotate90(image)

        image = flipNorthToSouth(image,24)

        for j in range(4):
            print("orientation %d"%(j+4))
            for r in range(-20,140):
                for c in range(-20,140):
                    ifSeaMonsterMarkPositions(image,r,c,monsters[0])
            image = rotate90(image)

        image = flipNorthToSouth(image,24)

        print(countHashes(image))

        writeImageToFile(image) # my_monster_output.txt
    """

    def test_loadRealFile(self):
        image = processInputFile( os.path.join(os.path.dirname(__file__),"output_without_borders.txt") )

        monsters = seaMonsters()

        print(monsters[0])

        for i in range(4):
            print("orientation %d"%(i))
            for r in range(-20,140):
                for c in range(-20,140):
                    ifSeaMonsterMarkPositions(image,r,c,monsters[0])
            image = rotate90(image)

        image = flipNorthToSouth(image,96)

        for j in range(4):
            print("orientation %d"%(j+4))
            for r in range(-20,140):
                for c in range(-20,140):
                    ifSeaMonsterMarkPositions(image,r,c,monsters[0])
            image = rotate90(image)

        image = flipNorthToSouth(image,96)

        print(countHashes(image))

        writeImageToFile(image) # my_monster_output.txt


if __name__ == '__main__':
    unittest.main()