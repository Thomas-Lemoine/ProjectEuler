
def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for x in range(3,int(n**0.5) + 1,2):
        if (n % x == 0):
            return False
    return True

def isPermutation(num1,num2):
    if len(str(num1)) != len(str(num2)):
        return False
    
    a = sorted(str(num1))
    str1 = "".join(a)
    b = sorted(str(num2))
    str2 = "".join(b)
    
    if str1 == str2:
        return True
    return False

#print(isPermutation(4333942,4323394))

def Main():
    for a in range(1000,(10000-3330*2)):
        b = 3330 + a
        c = 2*3330 + a
        if isPermutation(a, b) and isPermutation(b, c):
            if isPrime(a) and isPrime(b) and isPrime(c):
                print(str(a) + str(b) + str(c))
    
Main()