#Problem 57 : Square root convergents

def ans(n):
    ans = [1,2]
    for i in range(n):
        ans = inverse(frac_add(2,ans))
    ans = frac_add(1,ans)
    return ans


def frac_add(num,frac):
    return [num*frac[1] + frac[0], frac[1]]

def inverse(frac):
    return [frac[1], frac[0]]
    
def Main():
    total = 0
    for i in range(1,1000):
        frac = ans(i)
        if len(str(frac[0])) > len(str(frac[1])):
            total += 1
    print(total)

Main()