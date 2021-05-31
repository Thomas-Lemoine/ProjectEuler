
import math
from time import time
size = 6
start_time = time()

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   
                break        
            lower = x
        elif target < val:
            upper = x

timee = time()
listofprimes = primes_upto(10**size)
timeSieve = (time() - timee)

def Main():
    memo = {}
    
    for x in listofprimes:
        memo[x] = []
        valueprime = 10**(size - len(str(x)))
        #print(valueprime, x)
        if valueprime != 1:
            maxprime = int((valueprime//math.log(valueprime))*1.2)
        else:
            break
        firstbar = int(x//math.log(x))
        if firstbar < 20:
            firstbar = 0
        else:
            firstbar = firstbar
        for y in listofprimes[firstbar:maxprime]:#change this, utterly inefficient
            concat = int(str(x) + str(y))
            invconcat = int(str(y) + str(x))
            if (binary_search(listofprimes, concat) and
                binary_search(listofprimes, invconcat)):
                """if y not in memo.keys():
                    memo[y] = []
                memo[y].append(x)"""
                try:
                    memo[y].append(x)
                except KeyError:
                    memo[y] = []
                    memo[y].append(x)
                memo[x].append(y)
    mem1 = {}
    for i in memo.keys():
        if len(memo[i]) > 4:
            mem1[i] = memo[i]
    #print(mem1)
    for x in mem1.keys():
        for first in range(len(mem1[x])):
            for second in range(first+1,len(mem1[x])):
                for third in range(second+1,len(mem1[x])):
                    #for fourth in range(third+1, len(memo[x])):
                    try:
                        if (mem1[x][first] in mem1[mem1[x][second]] and
                        mem1[x][first] in mem1[mem1[x][third]] and
                        mem1[x][second] in mem1[memo[x][third]] 
                        #and mem1[x][first] in mem1[mem1[x][fourth]]
                        #and mem1[x][second] in mem1[mem1[x][fourth]] 
                        #and mem1[x][third] in mem1[mem1[x][fourth]]
                        ):
                            print(x,memo[x][first],memo[x][second],memo[x][third])
                            #,memo[x][fourth]
                    except KeyError:
                        print(x, first, second, third)
                        break
                            
    
    """if len(memo[x]) > 4:
            print(x, memo[x])"""
    """for key in memo.keys():
        for integer in memo[key]:
            if memo[integer] """
            
            
Main()

print(timeSieve)
print(time() - start_time)







""" for x in memo.keys():
        print(x)
        for first in range(len(memo[x])):
            for second in range(first+1,len(memo[x])):
                for third in range(second+1,len(memo[x])):
                    for fourth in range(third+1, len(memo[x])):
                        if (memo[x][first] in memo[memo[x][second]] and
                            memo[x][first] in memo[memo[x][third]] and
                            memo[x][second] in memo[memo[x][third]] 
                            and memo[x][first] in memo[memo[x][fourth]]
                            and memo[x][second] in memo[memo[x][fourth]] 
                            and memo[x][third] in memo[memo[x][fourth]]
                            ):
                            print(x,memo[x][first],memo[x][second],memo[x][third],memo[x][fourth])"""



"""for x in memo.keys():
        
        for first in range(len(memo[x])):
            for second in range(first+1,len(memo[x])):
                for third in range(second+1,len(memo[x])):
                    #for fourth in range(third+1, len(memo[x])):
                    if ((binary_search(memo[memo[x][second]], memo[x][first])) and
                        (binary_search(memo[memo[x][third]], memo[x][first])) and
                             #(binary_search(memo[memo[x][fourth]], memo[x][first])) and
                        (binary_search(memo[memo[x][third]], memo[x][second])) 
                             #and (binary_search(memo[memo[x][fourth]], memo[x][second])) and
                             #(binary_search(memo[memo[x][fourth]], memo[x][third]))
                        ):
                        print(x,memo[x][first],memo[x][second],memo[x][third])"""














