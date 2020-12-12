import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import followCourse

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue( getInputPath() )

    def test_mainInputFileLength(self):
        struct = processInputFile( getInputPath() )
        self.assertEqual(len(struct),795)

    def test_testInputFileLength(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input.txt"))
        self.assertEqual(len(struct),5)

    def test_followShort(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input.txt"))
        followCourse(struct)


if __name__ == '__main__':
    unittest.main()