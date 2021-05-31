from decimal import Decimal
from decimal import getcontext
b = 2000
getcontext().prec = b

def recCycle(n):
    lst = ''
    a = str(int(Decimal(10 ** b) / Decimal(n)))
    for i in range(15):
        lst = lst + a[i]
    #we have a list of the first 15 numbers of the decimal
    for x in range(15, len(a)-15):
        test = 0
        for i in range(15):
            if (a[x+i] == lst[i]):
                test += 1
        if test == 15:
            return x
    return 0

answer  = 0
for x in range(1,1000):
    if not((x%3==0) or (x%7==0)):
        if recCycle(x) > answer:
            answer = recCycle(x)
            a = x
print(f"{a} repeats itself over {answer} digits, so {a} is the answer!")