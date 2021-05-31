
def isDivisibleTiln(n):
    a = 1
    for x in range(11, n+1):
       i = a
       while a % x != 0:
           a += i
    print(a)

    
isDivisibleTiln(20)
                 