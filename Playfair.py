'''
@author William Ray Johnson
9/3/2017
'''

import PlayfairTable

class Playfair:
    
    
    def splitMessage(self, message):
        message = message.lower().replace(" ", "")
        splitMessage = ""
        
        for pair in range(len(message)//2):
            splitMessage = splitMessage + message[:2] + " "
            message = message[2:]
        
        if len(message) == 1:
            splitMessage = splitMessage + message + "x"
        elif len(message) == 0:
            splitMessage = splitMessage.rstrip()
            
        return splitMessage