
import math

def factorialsum(num):
    total = 0
    strnum = str(num)
    for x in range(0,len(strnum)):
        total += math.factorial(int(strnum[x]))
    return total

Sol = 0
for x in range(10,100000):
    if x == factorialsum(x):
        Sol += x
            
print(Sol)
