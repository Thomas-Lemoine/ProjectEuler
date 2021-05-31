
import math

def Dlst():
    low = 999
    up = 10001
    lst = []
    number = 0
    n = int(((((8*low + 1)**0.5) - 1)/2)+1) 
    while number < up:
        number = int(n*(n+1)/2)
        n += 1
        lst.append(number)
    lst.pop()
    return lst

def getminmax(prevstr):
    return (int(prevstr[2:]+'00'),int(str(int(prevstr[2:])+1)+'00'))

def isTri(x):
    return math.sqrt(8*x + 1) % 1 == 0

def isSqr(x):
    return math.sqrt(x) % 1 == 0

def isPen(x):
    return (1 + math.sqrt(24*x+1))/6 % 1 == 0

def isHex(x):
    return (1 + math.sqrt(8*x + 1))/4 % 1 == 0

def isHept(x):
    return (3 + math.sqrt(40*x + 9))/10 % 1 == 0

def isOcta(x):
    return (2 + math.sqrt(12*x + 4))/6 % 1 == 0

a = []
for n in range(1,70):
    a.append(n*(3*n - 2))
print(a)


for tri in Dlst():
    #print(tri)
    low = (tri%100)*100
    up = (tri%100)*100 + 100
    for sqr in range(low,up):
        if isSqr(sqr) and str(sqr)[-2] != '0' and len(str(sqr)) == 4:
            #print(sqr)
            low = (sqr%100)*100
            up = (sqr%100)*100 + 100
            for pen in range(low,up):
                if isPen(pen) and str(pen)[-2] != '0' and len(str(pen)) == 4:
                    low = (pen%100)*100
                    up = (pen%100)*100 + 100
                    for hexa in range(low,up):
                        if isHex(hexa) and str(hexa)[-2] != '0'  and len(str(hexa)) == 4:
                            low = (hexa%100)*100
                            up = (hexa%100)*100 + 100
                            for hept in range(low,up):
                                if isHept(hept) and str(hept)[-2] != '0'  and len(str(hept)) == 4:
                                    print(tri,sqr,pen,hexa,hept)
                                    low = (hept%100)*100
                                    up = (hept%100)*100 + 100
                                    for octa in range(low,up):
                                        if isOcta(octa) and (str(octa)[:2] == str(tri)[2:]):
                                            print(tri,sqr,pen,hexa,hept,octa)