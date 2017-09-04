'''
@author William Ray Johnson
9/3/2017
'''
import argparse

import Playfair

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrpyt a message using Playfair Cipher')
    parser.add_argument('-k', default="None", help="The keyword to be used in the cipher")
    args = parser.parse_args()
    if args.k == 'None':
        keyword = input("What is your keyword?: ")
    else:
        keyword = args.k
        
    cipher = Playfair.Playfair(keyword)
    
    option = input("Would you like to encrypt or decrypt a message?: ")
    message = input("What is the message you would like to " + option + "?: ")
    
    if option == 'encrypt' or option == 'Encrypt' or option[0] == 'e':
        splitMessage = cipher.splitMessage(message)
        newMessage = cipher.encrypt(splitMessage)
    if option == 'decrypt' or option == 'Decrypt' or option[0] == 'd':
        newMessage = cipher.decrypt(message)
    
    print("Here is your " + option + "ed message:")
    print(newMessage)
    
if __name__ == '__main__':
    main()