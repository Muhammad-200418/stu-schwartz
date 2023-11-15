#!/bin/python3

import sys, math, a_baseDic as bDic
import numpy as np

'''User will pass the plaintext and the key.
The key will be verified for errors by checking if the value passed does not contradict the possible values.
'''


def create_matrix(keystring):
    keys = keystring.split(" ")
    keymatrix = np.array([int(key) for key in keys]).reshape(2, 2)
    return keymatrix


def verify(keymatrix):
    # The determinant of matrix should have inverse defined.
    determinant = keymatrix[0][0] * keymatrix[1][1] - keymatrix[0][1] * keymatrix[1][0]
    if abs(determinant) % 26 in bDic.inverse:
        return True
    else:
        return False


def message_blocks(message):
    message = ''.join(message.split()).lower()
    if len(message) % 2 != 0:
        message += 'x'  # If input string is odd, make it even.
    block = [[], []]
    for i in range(0, len(message), 2):
        for key, value in bDic.dic.items():
            if value == message[i]:
                block[0].append(key)
    for i in range(1, len(message), 2):
        for key, value in bDic.dic.items():
            if value == message[i]:
                block[1].append(key)
    blocks = np.array(block)
    return blocks


def encrypt(matrix, message):
    blocks = message_blocks(message)  # Get the message in matrix form
    output = ""
    data = (matrix @ blocks) % 26
    for i in range(len(data[0])):  # Loop equal to length of one row of matrix
        output += bDic.dic[data[0][i]]  # Get the value from the multiplication and convert to strings
        output += bDic.dic[data[1][i]]  # Value are in the form, first value from row 1, second value from row 2.
        # This is because the complete message is encrypted in one go, rather than in blocks.
    return output


def inv_key(matrix):
    ad_joint = np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[
        0, 0]]]) % 26  # taking the adjoint, swapping 1 and 4 and change signs of 2 and 3
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # Find the determinant and take its inverse
    inv_Det = bDic.inverse[determinant % 26]
    dec_key = (inv_Det * ad_joint) % 26
    return dec_key


def count_digraph(message):
    message = ''.join(message.split()).lower()
    digraphs = {}
    trigraphs = {}
    for i in range(len(message) - 2):
        graphs = message[i:i + 2]
        if graphs in digraphs:
            digraphs[graphs] += 1
        else:
            digraphs[graphs] = 1

    for i in range(len(message) - 3):
        graphs = message[i:i + 3]
        if graphs in trigraphs:
            trigraphs[graphs] += 1
        else:
            trigraphs[graphs] = 1
    print(sorted(digraphs.items(), key=lambda digraph: digraph[1], reverse=True))
    print("\n\n")
    print(sorted(trigraphs.items(), key=lambda trigraph: trigraph[1], reverse=True))


def crunch(data):
    temp_1 = input("Please enter the plain text\n-->").split(" ")  # Enter the 2x1 matrix multiplied by key
    temp_2 = input("Please enter the cipher text\n-->").split(" ")  # Enter the Cipher Text matrix obtained
    eq_1 = []
    eq_2 = []
    for val in temp_1:
        for key, value in bDic.dic.items():
            if val == value:
                eq_1.append(key)
    for val in temp_2:
        for key, value in bDic.dic.items():
            if val == value:
                eq_2.append(key)

    ab = []
    cd = []
    for a in range(0, 25):
        for b in range(0, 25):
            val = (eq_1[0] * a + eq_1[1] * b) % 26
            if val == eq_2[0]:
                if a % 2 == 0 and b % 2 == 0:
                    pass
                else:
                    ab.append((a, b))
    print(eq_1, eq_2)
    for c in range(0, 25):
        for d in range(0, 25):
            val = (eq_1[0] * c + eq_1[1] * d) % 26
            if val == eq_2[1]:
                if c % 2 == 0 and d % 2 == 0:
                    pass
                else:
                    cd.append((c, d))

    keys = []
    for i in range(len(ab)):
        for j in range(len(cd)):
            res = (ab[i][0] * cd[j][1] - ab[i][1] * cd[j][0]) % 26
            if res % 2 != 0 and res % 13 != 0:
                keys.append((ab[i][0], ab[i][1], cd[j][0], cd[j][1]))

    possible_text = []
    for i in keys:
        matrix = create_matrix(f"{i[0]} {i[1]} {i[2]} {i[3]}")
        inverse = inv_key(matrix)
        possible_text.append(encrypt(inverse, data))

    for i in range(len(possible_text)):
        output = possible_text[i]
        output = ' '.join([output[i:i + 5] for i in
                           range(0, len(output), 5)]) + f"-->{keys[i][0]} {keys[i][1]} {keys[i][2]} {keys[i][3]}"
        if 'is' in output and 'the' in output:
            print(output)


# matrix = create_matrix("24 11 9 6")
# print(inv_key(matrix)) #14 9 5 4


# message = "Bob wants to go to great adventure tomorrow but i would rather go to the shore if we go to the amusement park we will spend all day in line"
# matrix = create_matrix("15 4 9 15")
# print(encrypt(matrix,message))


message = ("VTFWK UMESJ JYXUZ ANYWE VTJYV TCSLI CSTKE MKCZK WKKUK TYSQQ FIFTZ CNTMX IYSJE GSJKX QXSAA ZHQUJ YVFIU "
           "NOCML WLPUJ YUJAV AAVTT S")

count_digraph(message)
crunch(message)

# if len(sys.argv) < 4:
#     print('''Help Menu
#     - Run
#     python encrypt "2x2 Matrix key here" "Message goes here"
#     python decrypt "2x2 Matrix key here" "Message goes here"
#     python decrypt "0 0 0 0" "Message goes here" --> To Brute force
#     The key is the one with which matrix was encrypted.
#     ''')
#     sys.exit(0)
# else:
#     operation = sys.argv[1]
#     key = sys.argv[2]
#     payload = sys.argv[3]
#
#     matrix = create_matrix(key)
#     ver_key = verify(matrix)
#     if operation == 'encrypt':
#         if ver_key:
#             print(encrypt(matrix, payload))
#             print(f"Encrypted with \n{matrix}")
#             print(f"Decryption key is \n{inv_key(matrix)}")
#         else:
#             print("Matrix supplied is incorrect. Determinant must follow the law of multiplication")
#     elif operation == 'decrypt':
#         if key == '0 0 0 0':
#             pass
#         elif ver_key:
#             decryptionKey = inv_key(matrix)
#             print(encrypt(decryptionKey, payload))
#             print(f"Encrypted with \n{matrix}")
#             print(f"Decryption key is \n{decryptionKey}")
#         else:
#             print("Matrix supplied is incorrect. Determinant must follow the law of multiplication")
