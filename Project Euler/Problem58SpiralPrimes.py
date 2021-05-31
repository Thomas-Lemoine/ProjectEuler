# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:42:22 2021

@author: thoma
"""

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3,int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True



num = 1
numOfNums = 1
increment = 0
total = 0
for x in range(100000):
    increment += 2
    for i in range(4):
        #print(num)
        num += increment
        #print(numOfNums, "is num of nums")
        numOfNums += 1
        
        if isPrime(num):
            total += 1
        #print(total,"is total")
        #print(total/numOfNums)
    if ((total/numOfNums) < 0.1):
        #print(x)
        #print(total)
        #print(numOfNums)
        print(f"{increment + 1} is the answer!")
        break