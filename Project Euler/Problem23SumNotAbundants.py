
def isAbundant(n):
    sumDiv = 1
    if n == 1:
        return False
    for x in range(2, (int( n ** 0.5 ) + 1)):
        if (n % x == 0) and (n/x != x):
            sumDiv += x
            sumDiv += n/x
        elif (n % x == 0):
            sumDiv += x
    return (sumDiv > n)

abundantlst = []
for x in range(1,28123):
    if isAbundant(x):
        abundantlst.append(x)

lst = []
for x in abundantlst:
    for y in abundantlst:
        if x+y < 28123:
            lst.append(x+y)

lstOfSumAb = set(lst)
m = 28123 - 1
a = m*(m+1)/2

for x in lstOfSumAb:
    a -= x

print(int(a))