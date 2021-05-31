
def countDivisors(n):
    cnt = 0
    for i in range(1,int(n**(1/2)) + 1):
        if (n % i == 0):
            cnt += 2
            if n**(1/2) == i:
                cnt -= 1
    return cnt

i = 0
r = 0
answer = 0

while countDivisors(i) < 500:
    r += 1
    i += r

print(i)

"""def ListDiv(n):
    listDiv_lst = []
    for i in range(1,int(math.sqrt(n)) + 1):
        if (n % i == 0):
            listDiv_lst.append(i)
            listDiv_lst.append(int(n/i))
    listDiv_lst.sort()
    return listDiv_lst 
print("It has",len(ListDiv(i)), "factors")
#[print(countDivisors(n), n) for n in range(1,10)]"""