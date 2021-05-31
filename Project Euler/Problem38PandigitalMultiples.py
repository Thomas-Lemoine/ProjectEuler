
def ConcatenatedProduct(integer, n):
    strConc = ""
    for multip in range(0,n+1):
        strConc = strConc + str(multip*integer)
    return int(strConc)
  
def ContainsAllInts(num):
    for i in range(1,10):
        if not (str(i) in str(num)):
            return False
    return True
  
def Main():
    maxim = 0
    for integer in range(1,100000):
        lenint = len(str(integer))
        for n in range(1,int(10/lenint) + 5):
            if ConcatenatedProduct(integer, n) > 10**9:
                break
            prod = ConcatenatedProduct(integer, n)
            if ((ContainsAllInts(prod)) and (prod > maxim)):
                maxim = ConcatenatedProduct(integer, n)
                permint = integer
                permn = n
    print(maxim, "from", permint, "and", permn)

#fancy
if __name__ == '__main__':
    Main()

