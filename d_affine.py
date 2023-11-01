#!/bin/python3

# Take a message.
# Encipher or decipher it using affine.
# Verify the keys.
# Because the key unknown,try every possible key.
# Linguistic approach
import sys, math, a_baseDic as bDic, time


# Verifying that the multiplication key is correct
def verify(key):  # Checking if the number is co prime
    if math.gcd(key, 26) == 1 and key != 1:
        return True
    else:
        return False


def encrypt(a, b, text):
    if verify(a):
        text = ''.join(text.split()).lower()
        output = ""
        b = int(b) % 26
        for char in text:
            char = ((ord(char) - 96) % 26)
            char = ((char * a) + b) % 26
            output += bDic.dic[char]
        output = ' '.join([output[i:i + 5] for i in range(0, len(output), 5)])
        return output
    else:
        print(f"{a} is not a valid key")


def decrypt(a, b, message):
    c, d = reversal(a, b)
    return encrypt(c, d, message)


def reversal(a, b):
    c = bDic.inverse[a]
    d = ((26 - b) * c) % 26
    return c, d


# If we know what was the original key, we can find it out using reversal. However, otherwise, we have to brute force
# the key. To brute force, all we need is magnitude of repetition of characters, and boom. Brute force section below
def count_chars(text):
    counts = {}
    text = ''.join(text.split()).lower()
    for i in text:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts


def brute_force(cipher, expect, message):
    for a in bDic.mul:
        for b in range(0, 27):
            calc = (expect * a) + b
            index = calc % 26
            if cipher == index:
                c, d = reversal(a, b)
                print(f"{decrypt(a, b, message)}\n  {a},{b}  _  {c},{d}")


def crunch(message):
    data = count_chars(message)
    data = sorted(data.items(), key=lambda item: item[1], reverse=True)
    found = False
    while not found:
        print(data)
        C = (input("Please enter Cipher C: ")).lower()
        for key, val in bDic.dic.items():
            if val == C:
                C = key
        P = (input("Please enter plain text P: ")).lower()
        for key, val in bDic.dic.items():
            if val == P:
                P = key
        print("Brute forcing will print 11 possible output for each possible character. Check every entry. Starting "
              "now...")
        time.sleep(3)
        brute_force(C, P, message)
        done = input("Is is decoded? Enter Y to end, N to bruteforce again\n-->")
        while done != 'N' and done != 'Y':
            done = input("Please enter Y for yes and N for No\n-->")
        if done == 'Y':
            found = True


if len(sys.argv) < 4:
    print('''Help Menu
    - Windows
    python.exe d_affine.py encrypt a,b "Message"  
    python.exe d_affine.py decrypt a,b "Message"
    a,b are keys with which the message is encrypted.
    To Brute Force: python.exe d_affine.py decrypt 0,0 "Message"
    
    On linux, replace python.exe with python3
''')
    sys.exit(0)

else:
    action = sys.argv[1]
    a, b = sys.argv[2].split(",")
    a, b = int(a), int(b)
    payload = sys.argv[3]
    if action == 'encrypt':
        print(encrypt(a, b, payload))
    elif action == 'decrypt':
        if a == 0 and b == 0:
            crunch(payload)
        else:
            c, d = reversal(a, b)
            print(f"{decrypt(a, b, payload)}\n  {a},{b}  _  {c},{d}")
    else:
        print("Please select a valid action")
