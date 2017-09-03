'''
@author William Ray Johnson
9/3/2017
'''

import unittest

import Playfair

class PlayfairTest(unittest.TestCase):
    
    def setUp(self):
        self.cipher = Playfair.Playfair()
    
    def testSplitMessageWithOddLengthMessage(self):
        message = "This is a test"
        expectedSplit = "th is is at es tx"
        actualSplit = self.cipher.splitMessage(message)
        
        self.assertEqual(actualSplit, expectedSplit)
        
    def testSplitMessageWithEvenLengthMessage(self):
        message = "Hello World"
        expectedSplit = "he ll ow or ld"
        actualSplit = self.cipher.splitMessage(message)
        
        self.assertEqual(actualSplit, expectedSplit)
        
        
if __name__ == '__main__':
    unittest.main()