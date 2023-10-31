#!/bin/python3
import a_baseDic as bDic, sys

message = "My name is huzaifa"
index = 5

def encrypt(message,i):
    message = ''.join(message.split()).lower()
    cipherText = "" 
    i = int(i) % 26
    for char in message:
        char = ((ord(char) -96) % 26)
        char = (char * i) % 26
        cipherText += bDic.dic[char]
    cipherText = ' '.join([cipherText[i:i+5] for i in range(0, len(cipherText), 5)])
    print(cipherText)
    return cipherText 

def decrypt(message,i):
    message = ''.join(message.split()).lower()
    plainText = ""
    for char in message:
        char = (ord(char) - 96) % 26
        char = (char * i) % 26
        plainText += bDic.dic[char]
    plainText = ' '.join([plainText[i:i+5] for i in range(0, len(plainText), 5)])
    print(f"{plainText}_{bDic.inverse[i]}_{i}")
    return plainText    

message = sys.argv[2]
index = int(sys.argv[3])
print(index)
if (index%2 != 0 and index % 13 !=0) or (index == 0) :
    if sys.argv[1] == "encrypt":
        encrypt(message,index)
    elif index != '0' and index % 13 != 0:
        decrypt(message,index)
    elif index == 0:
        for i in range(1,26,2):
            if i % 13 !=0:
                decrypt(message,i)
    else:
        print("Hehe Nice try! Ok")
else:
    print("Hehe Nice try!")

#./c_multiplicative.py decrypt "DLANA GIUQN AUDIL COCHD TDCHG QLDKL UHHAR IGJUD DAH" 0

