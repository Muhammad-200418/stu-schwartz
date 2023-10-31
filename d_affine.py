#!/bin/python3

#Take a message.
#Encipher or decipher it using affine.
#Verify the keys.
#Because the key unknown,try every possible key. 
#Linguistic approach
import sys,math,a_baseDic as bDic

def verify(key):  #Checking if the number is co prime
	if math.gcd(key,26) == 1 and key != 1:
		return True
	else:
		return False

def encrypt(a,b,message):
	if verify(a):
		message = ''.join(message.split()).lower()
		cipherText = "" 
		b = int(b) % 26
		for char in message:
			char = ((ord(char) -96) % 26)
			char = ((char * a) + b) % 26
			cipherText += bDic.dic[char]
		cipherText = ' '.join([cipherText[i:i+5] for i in range(0, len(cipherText), 5)])
		print(cipherText)
		return cipherText 
	else:
		print(f"{a} is not a valid key")

def decrypt(a,b,message):
	encrypt(a,b,message)

def reversal(a,b):
	c = bDic.inverse[a]
	d = ((26-b) * c) % 26
	return c,d

#If we know what was the original key, we can find it out using reversal. However, otherwise, we have to brute force the key. 
#To brute force, all we need is magnitude of repitition of characters, and boom. 
def countChars(message):
	counts = {}
	message = ''.join(message.split()).lower() 
	for i in message:
		if i in counts:
			counts[i] += 1
		else:
			counts[i] = 1
	return(counts)

def bruteForce(cipher,expect,message):
	for a in bDic.mul:
		for b in range(1,27):
			if cipher == (((expect * a) + b) % 26): 
				c,d = reversal(a,b)
				decrypt(c,d,message)
				print(f"{a},{b}_{c},{d}")
				
def crunch(message):
	data = countChars(message)
	data = sorted(data.items(), key=lambda item: item[1],reverse=True)
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
		bruteForce(C,P,message)
# encrypt(15,17,"My name is Huzaifa")
# bruteForce(9,12,"gliid")

#./d_affine.py encrypt 9,12 "Message"
#./d_affine.py decrypt 9,12 "Message"
message = "NTYNC NSOGN XGNGQ NSNSN UIGEX GFNXG NGSMX GTUQZ TGQGF NQCNX SNXGM SFNSO GWKGQ NUCFQ"
# crunch(message)
# decrypt(0,0,message)
# Actually after updating it, it is now ./d_affine.py 

print(encrypt(13,2,"hello"))