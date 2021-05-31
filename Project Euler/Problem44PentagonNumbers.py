

def isPentagonal(p):
    if (((1 + (1 + 24*p)**0.5)/6) % 1 == 0):
        return True
    return False

def Pentagonal(n):
    return (int((n * (3 * n - 1))/2))


for i in range(1,10000):
    for j in range(1,i):
        if isPentagonal(Pentagonal(i) + Pentagonal(j)) and isPentagonal(Pentagonal(i) - Pentagonal(j)):
            print(Pentagonal(i) - Pentagonal(j), "from", i, "and", j)
