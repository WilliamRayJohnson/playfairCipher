'''
@author William Ray Johnson
9/3/2017
'''

import unittest

import Playfair

class PlayfairTest(unittest.TestCase):
    keyword = "test"
    
    def setUp(self):
        self.cipher = Playfair.Playfair(self.keyword)
    
    def testSplitMessageWithOddLengthMessage(self):
        message = "This is a test"
        expectedSplit = "th is is at es tx"
        actualSplit = self.cipher.splitMessage(message)
        
        self.assertEqual(actualSplit, expectedSplit)
        
    def testSplitMessageWithEvenLengthMessage(self):
        message = "Hello World"
        expectedSplit = "he lx lo wo rl dx"
        actualSplit = self.cipher.splitMessage(message)
        
        self.assertEqual(actualSplit, expectedSplit)
    
    def testSplitMessageWithEmptyMessage(self):
        message = ""
        expectedSplit = ""
        actualSplit = self.cipher.splitMessage(message)
        
        self.assertEqual(actualSplit, expectedSplit)
        
    def testSplitMessageWithSpaceMessage(self):
        message = "           "
        expectedSplit = ""
        actualSplit = self.cipher.splitMessage(message)
        
        self.assertEqual(actualSplit, expectedSplit)
        
    def testSplitMessageWithMatchingPair(self):
        message = "tree"
        expectedSplit = "tr ex ex"
        actualSplit = self.cipher.splitMessage(message)
        
        self.assertEqual(actualSplit, expectedSplit)
        
    def testEncryptWithWrapping(self):
        splitMessage = "he lx lo wo rl dx"
        expectedEncryption = "DB QS IQ VP QM FW"
        actualEncryption = self.cipher.encrypt(splitMessage)
        
        self.assertEqual(actualEncryption, expectedEncryption)
        
    def testEncrypt(self):
        splitMessage = "en cr yp tx"
        expectedEncryption = "BK GO WR SV"
        actualEncryption = self.cipher.encrypt(splitMessage)
        
        self.assertEqual(actualEncryption, expectedEncryption)
    
    def testDecrypt(self):
        encryptedMessage = "BK GO WR SV"
        expectedDecryption = "encryptx"
        actualDecryption = self.cipher.decrypt(encryptedMessage)
        
        self.assertEqual(actualDecryption, expectedDecryption)
        
    def testWikipediaExample(self):
        wikiCipher = Playfair.Playfair("playfair example")
        message = "Hide the gold in the tree stump"
        expectedSplit = "hi de th eg ol di nt he tr ex es tu mp"
        actualSplit = wikiCipher.splitMessage(message)
        
        self.assertEqual(actualSplit, expectedSplit)
        
        expectedEncryption = "BM OD ZB XD NA BE KU DM UI XM MO UV IF"
        actualEncryption = wikiCipher.encrypt(actualSplit)
        
        self.assertEqual(actualEncryption, expectedEncryption)
        
        
if __name__ == '__main__':
    unittest.main()