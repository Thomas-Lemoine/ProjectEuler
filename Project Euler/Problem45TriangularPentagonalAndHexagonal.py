
def isPent(p):
    if (((1 + (1 + 24*p)**0.5)/6) % 1 == 0):
        return True
    return False

def isHex(p):
    if (((1 + (1 + 8*p)**0.5)/4) % 1 == 0):
        return True
    return False

def Triangle(n):
    return int(n*(n+1)/2)

for n in range(1,100000):
    tr = Triangle(n)
    if isPent(tr) and isHex(tr):
        print(Triangle(n))