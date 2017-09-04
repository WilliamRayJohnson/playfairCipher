'''
@author William Ray Johnson
9/3/2017
'''

import PlayfairTable

class Playfair:
    def __init__(self, keyword):
        self.table = PlayfairTable.PlayfairTable(keyword)
    
    def splitMessage(self, message):
        message = message.lower().replace(" ", "")
        splitMessage = ""
        
        for pair in range(len(message)//2):
            if message[:2][0] == message[:2][1]:
                message = message[:1] + "x" + message[1:]
            splitMessage = splitMessage + message[:2] + " "
            message = message[2:]
        
        if len(message) == 1:
            splitMessage = splitMessage + message + "x"
        elif len(message) == 2:
            splitMessage = splitMessage + message
        elif len(message) == 0:
            splitMessage = splitMessage.rstrip()
            
        return splitMessage
        
    def encrypt(self, splitMessage):
        splitMessageArray = splitMessage.split(" ")
        encryptedMessage = ""
        
        for pair in splitMessageArray:
            charOneIndex = self.table.getIndex(pair[0])
            charTwoIndex = self.table.getIndex(pair[1])
            
            if charOneIndex[0] == charTwoIndex[0]:
                encryptedMessage = (encryptedMessage +
                                   self.table.getValue((charOneIndex[0], charOneIndex[1] + 1)) +
                                   self.table.getValue((charTwoIndex[0], charTwoIndex[1] + 1)) +
                                   " ")
            elif charOneIndex[1] == charTwoIndex[1]:
                encryptedMessage = (encryptedMessage +
                                   self.table.getValue((charOneIndex[0] + 1, charOneIndex[1])) +
                                   self.table.getValue((charTwoIndex[0] + 1, charTwoIndex[1])) +
                                   " ") 
            else:
                encryptedMessage = (encryptedMessage +
                                   self.table.getValue((charOneIndex[0], charTwoIndex[1])) +
                                   self.table.getValue((charTwoIndex[0], charOneIndex[1])) +
                                   " ")
        return encryptedMessage.rstrip().upper()