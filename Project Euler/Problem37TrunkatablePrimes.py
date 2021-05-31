
def isPrime(n):
    if n == 2:
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    for i in range(3,int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def isTrunkatablePrime(n):
    if not isPrime(n):
        return False
    strN = str(n)
    #from right
    if any([not isPrime(int(strN[:-i-1])) for i in range(len(str(n)) - 1)]):
        return False
    #from left
    if any([not isPrime(int(strN[i+1:])) for i in range(len(str(n)) - 1)]):
        return False
    return True

def Main():
    Sum = 0
    NumberOfAnswers = 0
    x = 10
    while not (NumberOfAnswers == 11) :
        if isTrunkatablePrime(x):
            Sum += x
            NumberOfAnswers += 1
        x += 1
    print(Sum)            
            
Main()
