import unittest
import os

from main import solvePalendromeWalk

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
        solvePalendromeWalk(grid,walk)


if __name__ == '__main__':
    unittest.main()