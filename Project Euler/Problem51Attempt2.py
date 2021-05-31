

#Problem51v02

def isPrime1(n):
    if (n == 2):
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    for i in range(3,int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True

def isPrime(n):
    if n == 1: 
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6-w
    return True
'''
def replaceW0(n,index1,index2):
    return (str(n)[:index1] + "0" + str(n)[index1:index2] + "0" + str(n)[index2:])

def adddigits(lenN,pos1,pos2):
    return 10**(lenN - pos1 + 1) + 10**(lenN - pos2)
'''

def replaceW0(n,index1,index2,index3):
    return (str(n)[:index1] + "0" + str(n)[index1:index2] + "0" + str(n)[index2:index3] + "0" +  str(n)[index3:]) 

def adddigits(lenN,pos1,pos2,pos3):
    return 10**(lenN - pos1 + 2) + 10**(lenN - pos2 + 1) + 10**(lenN - pos3)

def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes

def insertchar(LongNum,index1,index2,char):
    StrNum = str(LongNum)
    strchar = char
    if index2 < len(StrNum):
        return StrNum[:index1] + strchar + StrNum[index1:index2] + strchar + StrNum[index2:]
    else:
        return StrNum[:index1] + strchar + StrNum[index1:] + strchar
    
#very disappointing solve

def Main():
    totmax = 0
    lim = 8
    num = 0
    while totmax < lim:
        num += 1
        if num % 1000 == 0:
            print("benchmark :", num)
        lenN = len(str(num))
        for pos1 in range(0,lenN+1):
            for pos2 in range(pos1,lenN+1):
                for pos3 in range(pos2,lenN+1):
                    tempNum = int(replaceW0(num,pos1,pos2,pos3))
                    add = adddigits(lenN,pos1,pos2,pos3)
                    total = 0
                    if isPrime(tempNum) and pos1 != 0:
                        total += 1
                    for x in range(9):
                        tempNum = tempNum + add
                        if isPrime(tempNum):
                            total += 1
                    if total > totmax:
                        totmax = total 
                        print(replaceW0(num,pos1,pos2,pos3),"with the number",num)
import time
start = time.time()
Main()
print(time.time() - start)
#print(replaceW0(1234,3,3,4))
#print(adddigits(4,3,3,4))
"""
def Main():
    totmax = 0
    lim = 7
    num = 0
    while totmax < lim:
        num += 1
        if num % 1000 == 0:
            print("benchmark :", num)
        lenN = len(str(num))
        for pos1 in range(0,lenN+1):
            for pos2 in range(pos1,lenN+1):
                if (pos2 == lenN) and (str(num)[-1] == 2 or str(num)[-1] == 5):
                    break
                tempNum = int(replaceW0(num,pos1,pos2))
                add = adddigits(lenN,pos1,pos2)
                total = 0
                if isPrime(tempNum):
                    total += 1
                for x in range(9):
                    tempNum = tempNum + add
                    if isPrime(tempNum):
                        total += 1
                if total > totmax:
                    totmax = total 
                    print(replaceW0(num,pos1,pos2),"with the number",num)
                    
def Main1(primes):
    totmax = 0
    lim = 7
    num = 0
    while totmax < lim:
        num += 1
        if num % 1000 == 0:
            print("benchmark :", num)
        lenN = len(str(num))
        for pos1 in range(0,lenN+1):
            for pos2 in range(pos1,lenN+1):
                tempNum = int(replaceW0(num,pos1,pos2))
                add = adddigits(lenN,pos1,pos2)
                total = 0
                if (tempNum in primes):
                    total += 1
                for x in range(9):
                    tempNum = tempNum + add
                    if (tempNum in primes):
                        total += 1
                if total > totmax:
                    totmax = total 
                    print(replaceW0(num,pos1,pos2),"with the number",num)

def Main2():
    maxi = 0
    answer = ""
    num = 0
    while maxi < 7:
        num += 1
        lennum = len(str(num))
        for pos1 in range(0,lennum+1):
            for pos2 in range(pos1,lennum+2):
                total = 0
                for char in range(0,10):
                    if (isPrime(int(insertchar(num, pos1, pos2, str(char)))) and not (char == 0 and pos1 == 0)):
                        total += 1                        
                if total > maxi:
                    maxi = total
                    print(int(insertchar(num, pos1, pos2, str(char))))
                    for x in range(0,10):
                        if isPrime(int(insertchar(num, pos1, pos2, str(x)))):
                            answer = insertchar(num, pos1, pos2, str(x))
                            answer1 = insertchar(num, pos1, pos2, "*")
                            pos1perm = pos1
                            pos2perm = pos2
                            charperm = x
                            break
    print(maxi, "primes")
    print(answer, "is the number (with the 2 numbers added")
    print(answer1)
    print(charperm, "is the lowest number for replacing")
    print(pos1perm, "is the first position")
    print(pos2perm, "is the second position")




from timeit import default_timer
start = default_timer()
x = sieve_of_eratosthenes(100000)
print(default_timer() - start)
Main()
print(default_timer() - start)
#Main2()
#print(default_timer() - start)
#Main1(x)
#print(default_timer() - start)"""