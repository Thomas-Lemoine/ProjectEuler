def SumProperDivisors(n):
    answer = 1
    if (n == 1):
        return n
    for x in range(2,int(n**0.5) + 1):
        if (x ** 2 == n):
            answer += x
        elif (n % x == 0):
            answer += x
            answer += n/x
    return int(answer)

amicables = 0
for x in range(1,10000):
    sumDiv = SumProperDivisors(x)
    if (sumDiv > x) and ((SumProperDivisors(sumDiv)) == x):
            amicables += x + sumDiv
print(amicables)
