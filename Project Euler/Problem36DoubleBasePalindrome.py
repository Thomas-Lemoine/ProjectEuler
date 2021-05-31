#Problem 36
import math

def Binary(num):
    Binary = ""
    for x in range(int(math.log(num,2)) + 1):
        if (num % 2 == 1):
            Binary = "1" + Binary
            num -= 1
        else:
            Binary = "0" + Binary
        num /= 2
    return Binary
        
#print(Binary(585))

def isPal(n):
    return str(n) == (str(n))[::-1]

def Main():
    Sol = sum([x for x in range(1,10**6) if isPal(x) and isPal(Binary(x))])
    print(Sol)
    
Main()


        
        