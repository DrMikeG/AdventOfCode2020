import unittest
import os

"""

"""

class TestFactorialMethods(unittest.TestCase):

    def numbers1ToN(self,n):
        if (n == 0) :
            return [1]
        return range(1,n+1)


    def pleaseCalculateNFactorialForRecursive(self,n):
        # 4 factorial (4!) is defined as
        # 4 x 3 x 2 x 1
        # for any number > 0
        if n == 0 :
            return 1
        if n == 1 :
            return 1
        
        return n * self.pleaseCalculateNFactorialFor(n-1)

    def pleaseCalculateNFactorialFor(self,n):
        total = 1
        for i in self.numbers1ToN(n) : # [0,1,2,3,...,n-1]
            total = total * i
        return total

    def howManyDNATestsForNPeople(self,n):
        # Lets work out how many pairwise tests are needed to compare the DNA of n people
        # n!
        # __
        # 2x(n-2)!
        topOfFraction = self.pleaseCalculateNFactorialFor(n)
        bottomOfFraction = 2 * self.pleaseCalculateNFactorialFor(n-2)
        nTests = topOfFraction / bottomOfFraction
        return nTests

    def test_howManyTests2People(self):
        self.assertEqual(1,self.howManyDNATestsForNPeople(2))

    def test_howManyTests3People(self):
        self.assertEqual(3,self.howManyDNATestsForNPeople(3))

    def test_howManyTests4People(self):
        self.assertEqual(6,self.howManyDNATestsForNPeople(4))

    def test_howManyTests5People(self):
        self.assertEqual(10,self.howManyDNATestsForNPeople(5))

    def test_howManyTests33People(self):
        self.assertEqual(528,self.howManyDNATestsForNPeople(33))

    def test_howManyTests213People(self):
        self.assertEqual(22578,self.howManyDNATestsForNPeople(213))
    
    def test_howManyTests214People(self):
        self.assertEqual(22578+213,self.howManyDNATestsForNPeople(214))

    def test_howManyTests215People(self):
        self.assertEqual(22578+214+213,self.howManyDNATestsForNPeople(215))


    def test_howManyTests428People(self):
        self.assertEqual(68587,self.howManyDNATestsForNPeople(428)-self.howManyDNATestsForNPeople(213))

    def test_nIs0(self):
        self.assertEqual(1,self.pleaseCalculateNFactorialFor(0))

    def test_nIsOne(self):
        self.assertEqual(1,self.pleaseCalculateNFactorialFor(1))

    def test_nIsTwo(self):
        self.assertEqual(2,self.pleaseCalculateNFactorialFor(2))
    
    def test_nIsThree(self):
        self.assertEqual(6,self.pleaseCalculateNFactorialFor(3))

    def test_nIsFour(self):
        self.assertEqual(24,self.pleaseCalculateNFactorialFor(4))

    def test_nIs12(self):
        self.assertEqual(479001600,self.pleaseCalculateNFactorialFor(12))

    def test_nIs20(self):
        self.assertEqual(2432902008176640000,self.pleaseCalculateNFactorialFor(20))

    def test_nIs1500(self):
        self.pleaseCalculateNFactorialFor(1500)

    def test_nIs15000(self):
        self.pleaseCalculateNFactorialFor(15000)



if __name__ == '__main__':
    unittest.main()