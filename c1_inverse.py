#!/bin/python3
import sys

if len(sys.argv) < 2:
    print('''Please enter the number to calculate the inverse. 
Multiples of 2 and 13 are not allowed.
    

Windows
python.exe c1_inverse.py <Num>
Linux
./c1_inverse.py <Num>''')
    sys.exit(0)

num = int(sys.argv[1])
if num % 2 == 1 and num % 13 != 0:  # Multiples of 2 and 13 don't have an inverse
    for i in range(1, num + 1, 2):
        if i % 13 != 0:  # Only go for values that aren't multiples of 2 or 13
            found = False
            counter = 1
            while not found:
                if (i * counter) % 26 == 1:
                    found = True
                    print(f"Inverse of {i} is {counter}")
                else:
                    counter += 1
else:
    print("Please enter a valid number")
