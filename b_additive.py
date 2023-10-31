#!/bin/python3
import a_baseDic as bDic
import sys

def encrypt(message, i):
    i = int(i)
    message = ''.join(message.split()).lower()
    cipherText = ""
    for char in message:
        char = ((ord(char) - 96) % 26 + int(i)) % 26
        cipherText += bDic.dic[char]
    cipherText = ' '.join([cipherText[i:i + 5] for i in range(0, len(cipherText), 5)])
    return cipherText,i


# 1_additive.py encrypt message index
message = sys.argv[2]
index = sys.argv[3]
if sys.argv[1] == "encrypt":
    message,i = encrypt(message,index)
    print(message)
elif sys.argv[3] != '0':
    message,i = encrypt(message,index)
    print(f"{message}_{26 - i}_{i}")
else:
    for i in range(1, 26):
	    message,i = encrypt(message,i)
	    print(f"{message}_{26 - i}_{i}")

# For linux
# ./b_additive.py encrypt "Message goes here" 2
# ./b_additive.py decrypt "Message goes here" 24

# For windows
# python.exe b_additive.py encrypt "just a test" 2
