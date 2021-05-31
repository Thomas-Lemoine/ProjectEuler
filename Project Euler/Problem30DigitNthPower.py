def digitNthPow(n,power):
    total = 0
    if n == 1:
        return total
    for i in range(len(str(n))):
        total += int(str(n)[i])**power
    return total        

def findingSolutions(power):
    numsols = 0
    for x in range(1,1000000):
        if (digitNthPow(x, power) == x):
            numsols += x
            #print(x)
    print (numsols)
    
    
findingSolutions(5)