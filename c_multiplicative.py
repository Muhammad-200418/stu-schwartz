#!/bin/python3
import a_baseDic as bDic, sys


# If we encrypt the message twice, first with the key and then with the inverse of the key, we will get the original
# message
def encrypt(message, i):
    message = ''.join(message.split()).lower()
    output = ""
    i = int(i) % 26
    for char in message:
        char = ((ord(char) - 96) % 26)
        char = (char * i) % 26
        output += bDic.dic[char]
    output = ' '.join([output[i:i + 5] for i in range(0, len(output), 5)])
    return output


# print(len(sys.argv))
if len(sys.argv) < 4:
    print('''
- Windows
    python.exe c_multiplicative.py encrypt "Message goes here" 11
    python.exe c_multiplicative.py decrypt "Cipher goes here" 5
    To Brute Force: python.exe c_multiplicative.py decrypt "Cipher goes here" 0 
- Linux
    ./c_multiplicative.py encrypt "Message goes here" 11
    ./c_multiplicative.py decrypt "Cipher goes here" 5
    To Brute Force: ./c_multiplicative.py decrypt "Cipher goes here" 0''')
    sys.exit(0)

message = sys.argv[2]
index = int(sys.argv[3])
if (index % 2 != 0 and index % 13 != 0) or (index == 0):
    if sys.argv[1] == "encrypt":
        print(encrypt(message, index))
    elif index != 0:
        print(f"{encrypt(message, index)}_{bDic.inverse[index]}_{index}")
    else:
        for i in range(1, 26, 2):
            if i % 13 != 0:
                print(f"{encrypt(message, i)}_{bDic.inverse[i]}_{i}")
else:
    print("Hehe Nice try!")

# ./c_multiplicative.py decrypt "DLANA GIUQN AUDIL COCHD TDCHG QLDKL UHHAR IGJUD DAH" 0
