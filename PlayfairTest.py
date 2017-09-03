'''
@author William Ray Johnson
9/3/2017
'''

import unittest

import Playfair

class PlayfairTest(unittest.TestCase):
        
    def testCreateTable(self):
        keyword = "test"
        expectedTable = [['t','e','s','a','b'], 
                         ['c','d','f','g','h'], 
                         ['i','k','l','m','n'], 
                         ['o','p','q','r','u'],
                         ['v','w','x','y','z']]
                         
        actualTable = Playfair.createTable(keyword)
        self.assertEquals(expectedTable, actualTable)
        
        
if __name__ == '__main__':
    unittest.main()