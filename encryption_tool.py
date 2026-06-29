import time


## Visuals ---------------------------------------------------------------------------------------------------------------------------
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

art = r'''                                                                                                                    
:::::::-.    :::. :::::::::::::::.         .,:::::::::.    :::.  .,-::::: :::::::...-:.     ::-.::::::::::. ::::::::::::.,:::::: :::::::..   
 ;;,   `';,  ;;`;;;;;;;;;;'''';;`;;        ;;;;''''`;;;;,  `;;;,;;;'````' ;;;;``;;;;';;.   ;;;;' `;;;```.;;;;;;;;;;;'''';;;;'''' ;;;;``;;;;  
 `[[     [[ ,[[ '[[,   [[    ,[[ '[[,       [[cccc   [[[[[. '[[[[[         [[[,/[[['  '[[,[[['    `]]nnn]]'      [[      [[cccc   [[[,/[[['  
  $$,    $$c$$$cc$$$c  $$   c$$$cc$$$c      $$""""   $$$ "Y$c$$$$$         $$$$$$c      c$$"       $$$""         $$      $$""""   $$$$$$c    
  888_,o8P' 888   888, 88,   888   888,     888oo,__ 888    Y88`88bo,__,o, 888b "88bo,,8P"`        888o          88,     888oo,__ 888b "88bo,
  MMMMP"`   YMM   ""`  MMM   YMM   ""`      """"YUMMMMMM     YM  "YUMMMMMP"MMMM   "W"mM"           YMMMb         MMM     """"YUMMMMMMM   "W" '''.split('\n')


for i, line in enumerate(art):
    print(GREEN + line + '\033[0m')
    time.sleep(0.05)

print('')
print('')

## Functions ---------------------------------------------------------------------------------------------------------------------------
def shift_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') + int(shift)) % 26 + ord('A'))
    elif char.islower():
        return chr((ord(char) - ord('a') + int(shift)) % 26 + ord('a'))
    else:
        return char

def vigenere_encrypt(message, keyword):
    result = ''
    keyword_index = 0
    
    for char in message:
        if char.isalpha():
            keyword_letter = keyword[keyword_index % len(keyword)].upper()
            shift = ord(keyword_letter) - ord('A')
            result = result + shift_char(char, shift)
            keyword_index = keyword_index + 1
        else:
            result = result + char
    
    return result

def vigenere_decrypt(message, keyword):
    result = ''
    keyword_index = 0
    
    for char in message:
        if char.isalpha():
            keyword_letter = keyword[keyword_index % len(keyword)].upper()
            shift = ord(keyword_letter) - ord('A')
            result = result + shift_char(char, -shift)
            keyword_index = keyword_index + 1
        else:
            result = result + char
    
    return result


## Encryption tool --------------------------------------------------------------------------------------------------------------------
while True:
    
    method = input('Welcome user, caesar, vigenere or exit? ')
    if method == 'caesar':
        while True:
            answer = input('encrypt, decrypt, brute or home? ')
            if answer == 'encrypt':
                message = input('Message: ')
                shift = input('Key: ')
                message_encrypted = ''
                for char in message:
                    message_encrypted = message_encrypted + shift_char(char, int(shift))
                print(message_encrypted)

            elif answer == 'decrypt':
                message = input('Message: ')
                shift = input('Key: ')
                message_decrypted = ''
                for char in message:
                    message_decrypted = message_decrypted + shift_char(char, -int(shift))
                print(message_decrypted)
             
            elif answer == 'brute':
               message = input('Message: ')
               for shift in range(1, 26):
                   message_decrypted = ''
                   for char in message:
                       message_decrypted = message_decrypted + shift_char(char, -int(shift))
                   print(f'Key {shift}:', message_decrypted)
        
            elif answer == 'home':
                break

            else:
                print('Invalid request')
    elif method == 'vigenere':
        while True:
            answer = input('encrypt, decrypt or home? ')
            if answer == 'encrypt':
                message = input('Message: ')
                keyword = input('Keyword: ')
                message_encrypted = vigenere_encrypt(message, keyword)
                print(message_encrypted)
            
            elif answer == 'decrypt':
                message = input('Message: ')
                keyword = input('Keyword: ')
                message_decrypted = vigenere_decrypt(message, keyword)
                print(message_decrypted)
            
            elif answer == 'home':
                break

            else:
                print('Invalid request')
    elif method == 'exit':
        break

    else:
        print('Invalid request')