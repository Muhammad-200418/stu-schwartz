#!/bin/python3
import sys
num = int(sys.argv[1])+1
for i in range(1,num):
    if i%2 != 0 and i%13 !=0:
        found = False
        counter = 1
        while not found:
            if (i * counter) % 26 ==1:
                found = True
                print(f"Inverse of {i} is {counter}")
            else:
                counter += 1