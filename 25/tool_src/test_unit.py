import unittest
import os

from advent import calcLoopSize
from advent import calcEncryptionKey

class TestStringMethods(unittest.TestCase):

    def test_transform(self):
        self.assertEqual(8,calcLoopSize(5764801))
        self.assertEqual(11,calcLoopSize(17807724))


    def test_simpleLines(self):
        #The card and door use the wireless RFID signal to transmit the two public keys (your puzzle input) to the other device.
        #Now, the card has the door's public key, and the door has the card's public key. Because you can eavesdrop on the signal, you have both public keys, but neither device's loop size.
    
        #The card transforms the subject number of 7 according to the card's secret loop size. The result is called the card's public key.
        #The door transforms the subject number of 7 according to the door's secret loop size. The result is called the door's public key.

        loopSize = calcLoopSize(5764801)
        encKey = calcEncryptionKey(17807724, loopSize)
        self.assertEqual(14897079,encKey)

    def test_difficultFind(self):
        #The card and door use the wireless RFID signal to transmit the two public keys (your puzzle input) to the other device.
        #9093927
        #11001876
        #Now, the card has the door's public key, and the door has the card's public key. Because you can eavesdrop on the signal, you have both public keys, but neither device's loop size.
    
        #The card transforms the subject number of 7 according to the card's secret loop size. The result is called the card's public key.
        #The door transforms the subject number of 7 according to the door's secret loop size. The result is called the door's public key.

        loopSize = calcLoopSize(9093927)
        encKey = calcEncryptionKey(11001876, loopSize)
        print(encKey)
        self.assertEqual(12227206,encKey)
    
if __name__ == '__main__':
    unittest.main()