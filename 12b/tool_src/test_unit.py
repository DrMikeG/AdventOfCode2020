import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import followCourse
from advent import rotate90
from advent import rotate180
from advent import rotate270
from advent import rotateM90
from advent import rotateM180
from advent import rotateM270


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

    def test_rotate(self):
        self.assertEqual( rotate90(2,5),(5,-2) )
        self.assertEqual( rotate90(5,-2),(-2,-5) )
        self.assertEqual( rotate90(-2,-5),(-5,+2))
        self.assertEqual( rotate90(-5,+2),(+2,+5) )
        
        self.assertEqual( rotate180(2,5),(-2,-5) )
        self.assertEqual( rotate270(2,5),(-5,+2) )

    def test_rotateM(self):
        self.assertEqual( rotateM90(+5,-2),(+2,+5))
        self.assertEqual( rotateM90(-2,-5),(+5,-2))
        self.assertEqual( rotateM90(-5,+2),(-2,-5))
        self.assertEqual( rotateM90(+2,+5),(-5,+2))
        self.assertEqual( rotateM180(-2,-5),(2,5))
        self.assertEqual( rotateM270(-5,+2),(2,5))

    def test_defaultWayPoint1Step(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_2.txt"))
        self.assertEqual(11,followCourse(struct))
    
    def test_resetWayPointThen10Steps(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_3.txt"))
        self.assertEqual(0,followCourse(struct))

    def test_resetWayPointThenTriagle4(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_4.txt"))
        self.assertEqual(0,followCourse(struct))

    def test_resetWayPointThenTriagle5(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_5.txt"))
        self.assertEqual(0,followCourse(struct))

    def test_resetWayPointThenTriagle6(self):
        struct = processInputFile(os.path.join(os.path.dirname(__file__),"test_input_6.txt"))
        self.assertEqual(0,followCourse(struct))

if __name__ == '__main__':
    unittest.main()