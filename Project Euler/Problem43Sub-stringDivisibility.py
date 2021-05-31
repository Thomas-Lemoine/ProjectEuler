
from itertools import permutations

def tupleToStr(tup):
    str = "".join(tup)
    return str

def permutationsOf0to9():
    a = "0123456789"
    p = permutations(a)
    return p

def Main():
    Sol = 0
    for x in permutationsOf0to9():
        x = tupleToStr(x)
        if (x[0] != 0) and ((int(str(x)[1:4]) % 2 == 0) and (int(str(x)[2:5]) % 3 == 0) and (int(str(x)[3:6]) % 5 == 0) and (int(str(x)[4:7]) % 7 == 0) and (int(str(x)[5:8]) % 11 == 0) and (int(str(x)[6:9]) % 13 == 0) and (int(str(x)[7:10]) % 17 == 0)):
            Sol += int(x)
    print(Sol)

Main()