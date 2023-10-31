#!/bin/python3

import sys, math, a_baseDic as bDic
import numpy as np

'''User will pass the plaintext and the key.
The key will be verified for errors by checking if the value passed does not contradict the possible values.
'''


# e_hillDigraph.py encrypt "Message" 3_5_7_9

def verify(key):
    # Split it into individual key, convert to integer.
    # Check if it is co prime with 26
    matrix = key.split(" ")
    matrix = np.array([int(key) for key in matrix])  # Convert to integer
    matrix = matrix.reshape(2,2)
    print(int(np.linalg.det(matrix)))
    if abs(int(np.linalg.det(matrix))) in bDic.inverse:
        return True
    else:
        return False
print(verify("30 5 9 2"))
print(verify("9 2 30 5"))
# Verification complete. Prints the invalid key & returns False

# Adding the functionality to convert keys into np matrix
def createMatrix(keys):
    matrix = np.array(keys).reshape(2, 2)
    return matrix


def messageBlocks(message):
    message = message.lower()
    if len(message) % 2 != 0: message += 'x'  # If input string is odd, make it even.
    block = []
    for i in message:
        for key, value in bDic.dic.items():
            if value == i:
                block.append(key)
    blocks = [block[i:i + 2] for i in range(0, len(block), 2)]  # Split it into blocks of 2.
    blocks = np.array(blocks)
    blocks = blocks.reshape(-1, 2, 1)
    return blocks


def encrypt(keys, message):
    plainKeys = keys.split(" ")
    plainKeys = [int(key) for key in plainKeys]
    matrix = createMatrix(plainKeys)
    blocks = messageBlocks(message)
    encryptRaw = []
    for i in range(len(blocks)):
        data = (matrix @ blocks[i]) % 26
        encryptRaw.append(data[0][0])
        encryptRaw.append(data[1][0])
    cipher = ""
    for index in encryptRaw:
        cipher += bDic.dic[index]

    print(encryptRaw)
    print(cipher)


def invKey(keys):
    matrix = keys.split("_")
    matrix = [int(key) for key in matrix]  # Convert to integer
    matrix = createMatrix(matrix)
    adjoint = np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]]) % 26  # taking the adjoint
    determinant = int(np.linalg.det(matrix))  # Find the determinant and take its inverse
    determinant = bDic.inverse[determinant]
    deckey = (determinant * adjoint) % 26
    print(deckey)


# COnvert it into a 2x2 array. I might want to add functionality for 3x3, 4x4 and 5x5 matrix in future.
message = "LXNYQ DUYDQ LXENL XCFJK IGDQU WIMDC LXBIK UPTFQ QQWBT SUWMK TYLXO VKUKT YHALP WLXEZ PELXF AYXQG DEEML XDCQD VSAPA PSSUW CMAZQ GINYA XQQIE AVSAP APSSU WCMAZ QGINY AXQQI EA"
encrypt("9 5 2 11",message)

# encrypt("5_3_11_8","book")
# encrypt("16_7_17_23","clds")
# # print(verify("73_28_26_13"))
# invKey("5_3_11_8")


