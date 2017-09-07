'''
@author William Ray Johnson
9/3/2017
'''
from collections import OrderedDict

class PlayfairTable:
    
    alphabet = "abcdefghiklmnopqrstuvwxyz"

    def __init__(self, keyword):
        self.keyword = keyword.lower().replace(" ", "").replace("j", "i")
        self.createTable()
    
    '''
    @author William Ray Johnson
    Creates a table for a playfair cipher
    '''    
    def createTable(self):
        tableValues = "".join(OrderedDict.fromkeys(self.keyword + self.alphabet))
        table = [['-','-','-','-','-'], 
                 ['-','-','-','-','-'], 
                 ['-','-','-','-','-'], 
                 ['-','-','-','-','-'],
                 ['-','-','-','-','-']]
    
        for row in range(0,5):
            for column in range(0,5):
                table[row][column] = tableValues[0]
                tableValues = tableValues[1:]
    
        self.table = table
        
    def getTable(self):
        return self.table
        
    def getIndex(self, value):
        localValue = value
        if localValue == "j":
            localValue = "i"
        valueFound = False
        index = None
        row = 0
        column = 0
        
        while not(valueFound) and row <= 4:
            while not(valueFound) and column <= 4:
                if self.table[row][column] == localValue:
                    valueFound = True
                else:
                    column += 1
            if not(valueFound):
                column = 0
                row += 1
                
        if valueFound:
            return (row, column)
        else:
            raise ValueError('Value not found in table')
            
    def getValue(self, index):
        if index[0] == 5:
            index = (0, index[1])
        if index[1] == 5:
            index = (index[0], 0)
        return self.table[index[0]][index[1]]