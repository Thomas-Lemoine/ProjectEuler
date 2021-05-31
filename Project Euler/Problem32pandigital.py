
def isPandigital(n):
    return all(str(i+1) in str(n) for i in range(len(n)))

total = 0
st = set()
num = int(10**(9/2))
for x in range(1,num):
    for y in range(1,int(num/x)):
        c = x*y
        strTot = str(c) + str(x) + str(y)
        if (len(strTot) == 9) and isPandigital(strTot):
            st.add(c)
    total = sum(st)

print(f"{total} is the answer!")