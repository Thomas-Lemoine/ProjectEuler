
def primesfound(a,b):
    total = 0
    for n in range(1,1000):
        rep = n**2 + a*n + b
        if (rep > 0) and (isPrime(rep)):
            total += 1
        else:
            return total
    return total
    
def isPrime(num):
    if (num <= 1) or (num % 2 == 0):
        return False
    if (num == 2):
        return True
    for x in range(3,num):
        if (num % x == 0):
            return False
    return True


answer = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        if primesfound(a,b) > answer:
            answer = primesfound(a,b)
            perma = a
            permb = b
print(f"The answer is {answer} from {perma} and {permb} so the Problem's solution is {perma * permb}")