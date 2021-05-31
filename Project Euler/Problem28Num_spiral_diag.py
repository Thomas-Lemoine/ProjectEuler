def SpirDia(n):
    m = (n+1)/2
    total = 1
    increment = 1
    maximum = 1
    metaincrement = 0
    while maximum < m:
        #increases how much the numbers added increase every time
        metaincrement += 2
        #adds, each time the number is incremented (uh not english but ok)
        for i in range(4):
            increment += metaincrement
            total += increment
        #basically it works.
        maximum += 1
    return total
        
     
print(SpirDia(1001))