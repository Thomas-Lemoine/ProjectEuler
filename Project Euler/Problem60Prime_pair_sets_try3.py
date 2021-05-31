
#Problem 60 Euler attempt 3. I give up.
#import math
from time import time
import random,math
t0 = time()

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

primes = primes_upto(10000)

def comb(a, b):
    len_a = math.floor(math.log10(a))+1
    len_b = math.floor(math.log10(b))+1
    if is_prime(int(a*(10**len_b)+b)) and is_prime(int(b*(10**len_a)+a)):
        return True
    return False

def is_prime(n, k = 3):
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n % 2 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d % 2 == 0:
         s, d = s + 1, d >> 1
      # A for loop with a random sample of numbers
      for a in random.sample(range(2, n-2), k):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop

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

for a in primes:
    for b in primes:
        if b > a: 
            continue
        if comb(a,b):
            for c in primes:
                if c > b:
                    continue
                if comb(a,c) and comb(b,c):
                    for d in primes:
                        if d > c:
                            continue
                        if comb(a,d) and comb(b,d) and comb(c,d):
                            for e in primes:
                                if e > d:
                                    continue
                                if comb(a,e) and comb(b,e) and comb(c,e) and comb(d,e):
                                    print (a,b,c,d,e,a+b+c+d+e)
            
            

