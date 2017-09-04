'''
@author William Ray Johnson
9/3/2017
'''

import unittest

import PlayfairTable

class PlayfairTableTest(unittest.TestCase):
    expectedTable = [['t','e','s','a','b'], 
                     ['c','d','f','g','h'], 
                     ['i','k','l','m','n'], 
                     ['o','p','q','r','u'],
                     ['v','w','x','y','z']]
    keyword = "test"
    
    def setUp(self):
        self.table = PlayfairTable.PlayfairTable(self.keyword)
        
    def testCreateTable(self):
        self.assertEqual(self.expectedTable, self.table.getTable())
    
    def testGetIndex(self):
        actualIndex = self.table.getIndex('d')
        expectedIndex = (1,1)
        
        self.assertEqual(actualIndex, expectedIndex)
    
    def testGetValue(self):
        index = (3,2)
        expectedValue = 'q'
        actualValue = self.table.getValue(index)
        
        self.assertEqual(actualValue, expectedValue)
        
        
if __name__ == '__main__':
    unittest.main()