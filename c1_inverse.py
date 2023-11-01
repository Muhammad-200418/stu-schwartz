#!/bin/python3
import sys, a_baseDic as bDic

if len(sys.argv) < 2:
    print('''Please enter the number to calculate the inverse. 
Multiples of 2 and 13 are not allowed.
    
- Windows
python.exe c1_inverse.py <Num>
- Linux
./c1_inverse.py <Num>''')
    sys.exit(0)


def calcinverse(num):
    if num % 2 == 1 and num % 13 != 0:  # Multiples of 2 and 13 don't have an inverse
        key = num % 26
        inverse = bDic.inverse[key]
        return inverse
    else:
        print("Please enter a valid number.")
        sys.exit(0)
        


num = int(sys.argv[1])
print(f"The inverse of {num} is {calcinverse(num)}")
