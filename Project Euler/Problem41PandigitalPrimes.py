
def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True

def ContainsAllInts(num,lim):
    for i in range(1,lim+1):
        if not (str(i) in str(num)):
            return False
    return True

def Main():
    counter = 0
    start = 9876532
    x = start
    while counter == 0:
        if ContainsAllInts(x,len(str(x))) and isPrime(x):
            print(x)
            counter += 1
            
        x -= 1

Main()