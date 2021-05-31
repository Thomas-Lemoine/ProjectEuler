
import math
from time import time

expsize = 7
t0 = time()

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
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x
            
t1 = time()
listofprimes = primes_upto(10**expsize)
t2 = time()
timeSieve = (t2 - t1)


def Main():
    memo = {}
    
    for i in range(len(listofprimes)):
        for j in range(i+1,len(listofprimes)):
            prime1 = listofprimes[i]
            prime2 = listofprimes[j]
            concat = str(prime1) + str(prime2)
            if (len(concat) > expsize):
                break
            concat = int(concat)
            concat_inv = int(str(prime2) + str(prime1))
            if (binary_search(listofprimes, concat) and
                binary_search(listofprimes, concat_inv)):
                try:
                    memo[prime2].append(prime1)
                except KeyError:
                    memo[prime2] = []
                    memo[prime2].append(prime1)
                try:
                    memo[prime1].append(prime2)
                except KeyError:
                    memo[prime1] = []
                    memo[prime1].append(prime2)
    shortmemo = {}
    for i in memo.keys():
        if len(memo[i]) > 6:
            shortmemo[i] = memo[i]
    #print(shortmemo)
    
    for x in shortmemo.keys():
        print(x)
        for first in range(len(shortmemo[x])):
            for second in range(first+1,len(shortmemo[x])):
                for third in range(second+1,len(shortmemo[x])):
                    for fourth in range(third+1, len(shortmemo[x])):
                        try:
                            if (shortmemo[x][first] in shortmemo[shortmemo[x][second]] and
                                shortmemo[x][first] in shortmemo[shortmemo[x][third]] and
                                shortmemo[x][second] in shortmemo[shortmemo[x][third]] 
                                and shortmemo[x][first] in shortmemo[shortmemo[x][fourth]]
                                and shortmemo[x][second] in shortmemo[shortmemo[x][fourth]] 
                                and shortmemo[x][third] in shortmemo[shortmemo[x][fourth]]
                                ):
                                print(x,memo[x][first],memo[x][second],memo[x][third],memo[x][fourth])
                                #print(a,b,c,d,e)
                                return [x,memo[x][first],memo[x][second],memo[x][third],memo[x][fourth]]
                        except KeyError:
                            #print(x, first, second, third, fourth)
                            break
    
    """for prime1 in listofprimes:
        for prime2 in listofprimes:
            concat = str(prime1) + str(prime2)
            if len(concat) > expsize:
                break
            concat_inv = str(prime2) + str(prime1)
            if (binary_search(listofprimes, concat) and
                binary_search(listofprimes, concat_inv)):
                try:
                    memo[prime2].append(prime1)
                except KeyError:
                    memo[prime2] = []
                    memo[prime2].append(prime1)
                memo[prime1].append(prime2)"""
        



print(Main())










