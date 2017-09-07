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
        
    def testGetIndexOfJ(self):
        actualIndex = self.table.getIndex('j')
        expectedIndex = (2,0)
        
        self.assertEqual(actualIndex, expectedIndex)
    
    def testGetValue(self):
        index = (3,2)
        expectedValue = 'q'
        actualValue = self.table.getValue(index)
        
        self.assertEqual(actualValue, expectedValue)
        
    def testGetValueOutOfRangeRow(self):
        index = (5,2)
        expectedValue = 's'
        actualValue = self.table.getValue(index)
        
        self.assertEqual(actualValue, expectedValue)
        
    def testGetValueOutOfRangeColumn(self):
        index = (4,5)
        expectedValue = 'v'
        actualValue = self.table.getValue(index)
        
        self.assertEqual(actualValue, expectedValue)
    
    def testCreateTableKeywordWithJ(self):
        expectedTable = [['i','a','c','k','b'], 
                         ['d','e','f','g','h'], 
                         ['l','m','n','o','p'], 
                         ['q','r','s','t','u'],
                         ['v','w','x','y','z']]
        actualTable = PlayfairTable.PlayfairTable("jack").getTable()
        
        self.assertEqual(actualTable, expectedTable)
        
        
if __name__ == '__main__':
    unittest.main()