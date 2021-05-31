
def isPrime(n):
    if (n == 2):
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    for i in range(3,int(n**0.5) + 1,2):
        if (n % i == 0):
            return False
    return True

total = -10
for x in range(2,10000):
    if total > 1000000:
        break
    if isPrime(x):
        total += x
        if isPrime(total):
            print(total)
            
"""
958577
920291
978037
997651


"""