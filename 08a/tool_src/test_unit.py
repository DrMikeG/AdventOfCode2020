import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import processInstruction

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue(os.path.exists(getInputPath()))

    def test_inputFileLength(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(len(struct),611)

    def test_instruction_acc_01(self):
        accumulator = 0
        programCounter = 0
        state = processInstruction(('acc',1),(programCounter,accumulator))
        self.assertEqual(state[0],1)
        self.assertEqual(state[1],1)

    def test_instruction_acc_02(self):
        accumulator = 0
        programCounter = 0
        state = processInstruction(('acc',-1),(programCounter,accumulator))
        self.assertEqual(state[0],1)
        self.assertEqual(state[1],-1)
 
    def test_instruction_nop_01(self):
        accumulator = 0
        programCounter = 0
        state = processInstruction(('nop',1),(programCounter,accumulator))
        self.assertEqual(state[0],1)
        self.assertEqual(state[1],0)

    def test_instruction_jmp_01(self):
        accumulator = 0
        programCounter = 0
        state = processInstruction(('jmp',1),(programCounter,accumulator))
        self.assertEqual(state[0],1)
        self.assertEqual(state[1],0)

    def test_instruction_jmp_02(self):
        accumulator = 0
        programCounter = 0
        state = processInstruction(('jmp',2),(programCounter,accumulator))
        self.assertEqual(state[0],2)
        self.assertEqual(state[1],0)

    def test_instruction_jmp_03(self):
        accumulator = 0
        programCounter = 0
        state = processInstruction(('jmp',-2),(programCounter,accumulator))
        self.assertEqual(state[0],-2)
        self.assertEqual(state[1],0)

if __name__ == '__main__':
    unittest.main()