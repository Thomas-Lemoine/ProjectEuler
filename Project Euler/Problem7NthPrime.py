
def isPrime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

def primeList(n):
    primes = []
    totalprimes = 0
    x = 2
    while totalprimes <= n:
        if isPrime(x):
            primes.append(x)
            totalprimes += 1
        x += 1
    return primes
    
def NthPrime(n):
    print(primeList(n)[n-1])
    
#This is slow
NthPrime(10001)