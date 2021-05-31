
import math, time, random

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x
            
def isCyclic(lst):
    if not lst[0][:2] == lst[-1][2:]:
        return False
    for i in range(len(lst) - 1):
        if not lst[i][2:] == lst[i+1][:2]:
            print(lst[i][2:], lst[i+1][:2],i)
            return False
    return True

def getminmax(prevstr):
    return (int(prevstr[2:]+'00'),int(str(int(prevstr[2:])+1)+'00'))

def Dlst(d,lowup):
    low = lowup[0] - 1
    up = lowup[1] + 1
    lst = []
    number = 0
    if d == 3:
        n = int(((((8*low + 1)**0.5) - 1)/2)+1) 
        while number < up:
            number = int(n*(n+1)/2)
            n += 1
            lst.append(str(number))
            
    if d == 4:
        n = int(math.sqrt(low)+1) 
        while number < up:
            number = int(n*n)
            n += 1
            lst.append(str(number))
    if d == 5:
        n = int(((((24*low + 1)**0.5) + 1)/6)+1) 
        print(n)
        while number < up:
            number = int(n*(n+1)/2)
            n += 1
            lst.append(str(number))
    if d == 6:
        n = int(((((8*low + 1)**0.5) + 1)/4)+1) 
        while number < up:
            number = int(n*(n+1)/2)
            n += 1
            lst.append(str(number))
            
    if d == 7:
        n = int(((((40*low + 9)**0.5) + 3)/10)+1) 
        while number < up:
            number = int(n*(n+1)/2)
            n += 1
            lst.append(str(number))
            
    if d == 8:
        n = int(((((12*low + 4)**0.5) + 2)/6)+1) 
        while number < up:
            number = int(n*(n+1)/2)
            n += 1
            lst.append(str(number))
    lst.pop()
    return lst


#low = "3000"
#limit = "3100"
#lowup = (low,limit)
#print(Dlst(4,(1000,10000)))
#trilst = Dlst(3,lowup)
#print(trilst)
#sqrlst = Dlst(4,lowup)
#penlst = Dlst(5,low,limit)
#hexlst = Dlst(6,low,limit)
#heptlst = Dlst(7,low,limit)
#octlst = Dlst(8,low,limit)
#print(sqrlst)
"""
['2025', '2116', '2209', '2304', '2401', '2500', '2601',
 '2704', '2809', '2916', '3025', '3136', '3249', '3364',
 '3481', '3600', '3721', '3844', '3969', '4096', '4225',
 '4356', '4489', '4624', '4761', '4900', '5041', '5184',
 '5329', '5476', '5625', '5776', '5929', '6084', '6241',
 '6400', '6561', '6724', '6889', '7056', '7225', '7396',
 '7569', '7744', '7921', '8100', '8281', '8464', '8649',
 '8836', '9025', '9216', '9409', '9604', '9801', '10000']"""

print(Dlst(5,(10000,8300)))
"""
for tri in Dlst(3,(1000,10000)):
    lowuptri = getminmax(tri)   
    #print(tri, lowuptri, Dlst(4,lowuptri))
    for sqr in Dlst(4,lowuptri):
        lowupsqr = getminmax(sqr)
        for pen in Dlst(5,lowupsqr):
            lowuppen = getminmax(pen)
            for hexa in Dlst(6,lowuppen):
                lowuphexa = getminmax(hexa)
                for hept in Dlst(7,lowuphexa):
                    lowuphept = getminmax(hept)
                    print(tri,sqr,pen,hexa,hept)
                    for octa in Dlst(8,lowuphept):
                        if octa[:2] == tri[2:]:
                            print(tri,sqr,pen,hexa,hept,octa)"""
                        