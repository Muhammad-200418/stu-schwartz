#!/bin/python3
import a_baseDic as bDic
import sys


# In addition cipher, we are just rotating the letters. That's why it's also called shift cipher.
# If we rotate letter 'a' by 3 to get 'd', one way to get back is by going back 3 alphabets.
# However, we can move 23 alphabets farther and will still reach back to the alphabet 'a'
# This allows us to simplify our functions and the process of decryption.
def rotate(message, i):
    i = int(i)
    message = ''.join(message.split()).lower()  # Remove whitespaces, join it, convert to lowecase
    output = ""
    for char in message:
        char = ((ord(char) - 96) % 26 + int(i)) % 26  # From ASCII to its respective index, adds the shift
        output += bDic.dic[char]  # Use the dictionary in a_basedic to convert the index to a character to be displayed.
    output = ' '.join([output[i:i + 5] for i in range(0, len(output), 5)])  # Split in the blocks of 5
    return output, i


if len(sys.argv) < 4:
    print('''
python b_additive.py encrypt "PlainText goes here" 2
python b_additive.py decrypt "CipherText goes here" 24
    ''')
    sys.exit(0)

message = sys.argv[2]  # Passed in as third argument on cmd
index = sys.argv[3]  # Fourth argument on cmd
if sys.argv[1] == "encrypt":
    outputMessage, i = rotate(message, index)
    print(outputMessage)
elif sys.argv[3] != '0':
    outputMessage, i = rotate(message, index)
    print(f"{outputMessage}_{26 - i}_{i}")
else:
    for j in range(1, 26):
        outputMessage, i = rotate(message, j)
        print(f"{outputMessage}_{26 - i}_{i}")
