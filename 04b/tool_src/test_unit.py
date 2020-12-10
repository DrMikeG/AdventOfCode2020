import unittest
import os

from main import solvePalendromeWalk
from main import countSnakeCellsNESWOfCell
from main import countSnakeCellsIn8OfCell
class TestStringMethods(unittest.TestCase):

    def test_program_solvePalendromeWalk(self):
        grid = []
        grid.append([9, 9, 9, 9, 9, 9, 9, 9, 9])
        grid.append([9, 9, 9, 9, 9, 9, 9, 9, 9])
        grid.append([8, 8, 8, 8, 8, 9, 9, 9, 9])
        grid.append([8, 8, 4, 5, 6, 8, 9, 9, 9])
        grid.append([1, 2, 3, 8, 7, 9, 9, 9, 9])
        grid.append([8, 8, 9, 9, 6, 9, 9, 9, 9])
        grid.append([9, 9, 3, 4, 5, 9, 9, 9, 9])
        grid.append([9, 1, 2, 3, 9, 9, 9, 9, 9])
        grid.append([9, 9, 9, 9, 9, 9, 9, 9, 9])

        walk = []
        walk.append(((4,0),(7,1)))
        #solvePalendromeWalk(grid,walk)

    def test_program_solvePalendromeWalk2(self):
        grid = []
        grid.append([5, 1, 4, 3, 7, 9, 8, 2, 6])
        grid.append([2, 9, 8, 6, 1, 5, 3, 4, 0])
        grid.append([7, 6, 3, 2, 8, 4, 5, 9, 1])
        grid.append([6, 3, 2, 1, 4, 8, 9, 7, 5])
        grid.append([8, 5, 1, 9, 6, 7, 2, 3, 4])
        grid.append([4, 7, 9, 5, 3, 2, 1, 6, 8])
        grid.append([9, 4, 6, 8, 2, 1, 7, 5, 3])
        grid.append([3, 8, 5, 7, 9, 6, 4, 1, 2])
        grid.append([1, 2, 7, 4, 5, 3, 6, 8, 9])

        walk = [((4, 0), (7, 1)), ((4, 1), (7, 2)), ((5, 1), (7, 3)), ((5, 2), (7, 4)), ((5, 3), (8, 4)), ((5, 4), (8, 5)), ((4, 4), (8, 6)), ((3, 4), (7, 6)), ((3, 3), (7, 7)), ((2, 3), (7, 8)), ((2, 2), (6, 8)), ((1, 2), (5, 8)), ((0, 2), (4, 8)), ((0, 3), (4, 7)), ((0, 4), (3, 7)), ((0, 5), (3, 6)), ((1, 5), (2, 6)), ((1, 6), (1, 6))]
        #self.assertEquals( countSnakeCellsNESWOfCell((4, 1),walk), 2)
        #self.assertEquals( countSnakeCellsIn8OfCell((3, 1), walk), 6 )
        
        self.assertTrue(solvePalendromeWalk(grid,walk))
        



if __name__ == '__main__':
    unittest.main()