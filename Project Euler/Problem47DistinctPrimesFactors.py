def isPrime(n):
    if (n == 2):
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    for i in range(3,int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True

def lstPrime():
    lstPrime = []
    for n in range(1,10000):
        if isPrime(n):
            lstPrime.append(n)
    return lstPrime


def primeFactList(lstPrime):
    lstPrimeFact = []
    for x in range(1,150000):
        total = 0
        for prime in lstPrime:
            if prime > x:
                break
            if (x % prime == 0):
                total += 1
        if total == 4:
            lstPrimeFact.append(x)
    return lstPrimeFact

lstPrimeFact = primeFactList(lstPrime())
for i in range(10, len(lstPrimeFact) - 4):
    if lstPrimeFact[i] == lstPrimeFact[i+1] - 1 == lstPrimeFact[i+2] - 2 == lstPrimeFact[i+3] - 3:
        print(lstPrimeFact[i])