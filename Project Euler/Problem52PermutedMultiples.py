
def samedigits(n1,n2):
    sn1 = sorted(str(n1))
    sn2 = sorted(str(n2))
    if sn1 == sn2:
        return True
    return False

def fits_answer(x):
    for i in range(2,7):
        if not samedigits(x, x*i):
            return False
    return True

def Main():    
    for x in range(1,1000000):
        if fits_answer(x):
            print(x)

Main()
            