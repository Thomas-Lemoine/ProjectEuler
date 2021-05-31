def NumOfSulutions(p):
    numSols = 0
    for a in range(1,(int(p * (2 - (2**0.5))/2)) + 1):
        b = ((p**2) - 2*p*a)/((2*p) - (2*a))
        c = ((a**2) + (b**2))**0.5
        if (a % 1 == 0) and (b % 1 == 0) and (c % 1 == 0):
            numSols += 1
    return numSols

def Main():
    maximum = 0
    for x in range(1001):
        if (NumOfSulutions(x) > maximum):
            maximum = NumOfSulutions(x)
            final_ans = x
    print(f"{final_ans} is the answer!")
            

Main()