
from math import factorial

def choose(n,r):
    return int(factorial(n)/(factorial(r) * factorial(n-r)))

def Main():
    total = 0
    for n in range(1,101):
        for r in range(1,n):
            if choose(n,r) > 1000000:
                total += 1
    print(total)
    
Main()