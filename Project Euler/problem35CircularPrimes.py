def isPrime(n):
    if n == 2:
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    for x in range(3,int(n**0.5)+1,2):
        if (n % x == 0):
            return False
    return True

def rotate(stringNum):
    return stringNum[-1] + stringNum[:-1]

def isCircularPrime(num):
    numstr = str(num)
    return all([isPrime(int((numstr := rotate(numstr)))) for i in range(len(numstr))])
       
def Main():
    Sol = 0
    for x in range(0,10**6):
        Sol += 1 if isCircularPrime(x) else 0
    print(Sol)
    
Main()
    