def isPrime(n):
    if (n == 2):
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    for i in range(3,int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True

def Main():
    #PrimeList :
    primelst = []
    for testforPrime in range(1,100000):
        if isPrime(testforPrime):
            primelst.append(testforPrime)
    for odd in range(3,10000,2):
        if not isPrime(odd):
            composite = odd
            total = 0
            for prime in primelst:
                if (prime > composite):
                    break
                if ((((composite - prime)/2)**0.5) % 1 == 0):
                    total += 1
            if total == 0:
                print(composite)
                #makes the Main stop
                return True

Main()