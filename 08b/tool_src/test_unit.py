import unittest
import os

from advent import getInputPath
from advent import processInputFile
from advent import processInstruction
from advent import indicesOfJmps
from advent import indicesOfNops
from advent import processStruct
from advent import changeOperation

class TestStringMethods(unittest.TestCase):

    def test_isFile(self):
        self.assertTrue(os.path.exists(getInputPath()))

    def test_inputFileLength(self):
        struct = processInputFile(getInputPath())
        self.assertEqual(len(struct),611)
        self.assertEqual(len(indicesOfJmps(struct)),225)
        self.assertEqual(len(indicesOfNops(struct)),56)

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

    def test_program_01(self):
        struct= [("nop",+0),("acc",+1),("jmp",+4),("acc",+3),("jmp",-3),("acc",-99),("acc",+1),("jmp",-4),("acc",+6)]
        processStruct(struct)

    def test_program_02(self):
        struct= [("nop",+0),("acc",+1),("jmp",+4),("acc",+3),("jmp",-3),("acc",-99),("acc",+1),("jmp",-4),("acc",+6)]
        changeOperation(struct,0)
        self.assertEqual(struct[0][0],"jmp")
        self.assertFalse(processStruct(struct))

    def test_program_03(self):
        struct= [("nop",+0),("acc",+1),("jmp",+4),("acc",+3),("jmp",-3),("acc",-99),("acc",+1),("jmp",-4),("acc",+6)]
        changeOperation(struct,7)
        self.assertEqual(struct[7][0],"nop")
        self.assertTrue(processStruct(struct))


if __name__ == '__main__':
    unittest.main()