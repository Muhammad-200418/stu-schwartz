#!/bin/python3
import a_baseDic as bDic
import sys


def decrypt(message, i):
    i = int(i)
    message = ''.join(message.split()).lower()
    plainText = ""
    for char in message:
        char = ((ord(char) - 96) % 26 + int(i)) % 26
        plainText += bDic.dic[char]
    plainText = ' '.join([plainText[i:i + 5] for i in range(0, len(plainText), 5)])
    print(f"{plainText}_{26 - i}_{i}")
    return plainText


def encrypt(message, i):
    message = ''.join(message.split()).lower()
    cipherText = ""
    for char in message:
        char = ((ord(char) - 96) % 26 + int(i)) % 26
        cipherText += bDic.dic[char]
    cipherText = ' '.join([cipherText[i:i + 5] for i in range(0, len(cipherText), 5)])
    print(cipherText)
    return cipherText


# 1_additive.py encrypt message index
message = sys.argv[2]
if sys.argv[1] == "encrypt":
    index = sys.argv[3]
    encrypt(message, index)
elif sys.argv[3] != '0':
    index = sys.argv[3]
    print(f"{encrypt(message, i)}_{26 - i}_{i}")
else:
    for i in range(1, 26):
        print(f"{encrypt(message, i)}_{26 - i}_{i}")

# ./b_additive.py encrypt "Message goes here" 2
# ./b_additive.py decrypt "Message goes here" 24

# For windows
# python.exe b_additive.py encrypt "just a test" 2
