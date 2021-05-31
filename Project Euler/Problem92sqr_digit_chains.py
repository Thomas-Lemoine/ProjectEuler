import time

total = 0
memo = {}
t1 = time.time()
for num in range(1,10000000):
    x = num
    while x != 1 and x != 89:
        if x in memo:
            x = memo[x]
        else:
            x = sum([int(n)**2 for n in str(x)])    
    if num < 1000:
        memo[num] = x
    if x == 89:
        total += 1
print(total, time.time() - t1)