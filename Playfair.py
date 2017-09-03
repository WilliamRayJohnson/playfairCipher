'''
@author William Ray Johnson
9/3/2017
'''
from collections import OrderedDict

'''
@author William Ray Johnson
Creates a table for a playfair cipher
'''
def createTable(keyword):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    tableValues = "".join(OrderedDict.fromkeys(keyword + alphabet))
    table = [['-','-','-','-','-'], 
             ['-','-','-','-','-'], 
             ['-','-','-','-','-'], 
             ['-','-','-','-','-'],
             ['-','-','-','-','-']]
    
    for row in range(0,5):
        for column in range(0,5):
            table[row][column] = tableValues[0]
            tableValues = tableValues[1:]
    
    return table