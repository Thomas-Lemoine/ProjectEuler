import time
start_time = time.time()


def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

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
timee = time.time()
listofprimes = primes_upto(10000000)
timeSieve = (time.time() - timee)
#print(listofprimes)



def split(prime, listofprimes,integerform):
    answer = []
    lenprime = len(str(prime))
    strprime = str(prime)
    for i in range(1,lenprime):
        listsplit = [int(strprime[:i]), int(strprime[i:])]
        reverseprime = str(listsplit[1]) + str(listsplit[0])
        if ((binary_search(listofprimes, listsplit[0])) and
            (binary_search(listofprimes, listsplit[1])) and
            (binary_search(listofprimes, int(reverseprime)))):
            if int(reverseprime) > prime:
                if integerform:
                    answer.append([int(strprime[:i]),int(strprime[i:])])
                    answer.append([int(strprime[i:]),int(strprime[:i])])
                else:
                    answer.append([strprime[:i], strprime[i:]])
                    answer.append([strprime[i:], strprime[:i]])
    return answer

#print(listofprimes[:10**1])

#print(split(6737,listofprimes,True))

def match(n,lst):
    lst1 = [n,[]]
    for sublist in lst:
        if sublist[0] == n:
            lst1[1].append(int(sublist[1]))
    if len(lst1[1]) > 3:
        lst1[1] = sorted(list(set(lst1[1])))
        print(lst1)


"""
array = list()
for x in range(1,10000):
    array.append([x])
#print(array)
lst = []
for prime in listofprimes[:10**5]:
    listx = split(prime, listofprimes,True)
    if listx != []:
        for sublist in listx:
            array[sublist[0]].append(sublist[1])

print(array)        
#print(lst)"""

def Main():
    allthelists = time.time()
    lst = []
    for prime in listofprimes[:10**6]:
        listx = split(prime, listofprimes,True)
        if listx != []:
            lst += listx
    alltheliststime = allthelists - time.time()
    #print(lst)
    for x in listofprimes[:1000]:
        match(x,lst)
    print(alltheliststime)

Main()

"""
def split(prime, listofprimes):
    answer = []
    lenprime = len(str(prime))
    #print(lenprime, "is lenprime")
    strprime = str(prime)
    #print(strprime, "is strprime")
    for i in range(1,lenprime):
        #print((strprime[-i:] + strprime[:-i]),"haha")
        #print((int(strprime[:i]) in listofprimes))
        #print((int(strprime[i:]) in listofprimes))
        #print((int(strprime[-i+1:] + strprime[:-i+1]) in listofprimes))
        if ((int(strprime[:i]) in listofprimes) and (int(strprime[i:]) in listofprimes)
            and (int(strprime[-i+1:] + strprime[:-i+1]) in listofprimes)):
            #print(strprime[i:], "for [i:]")
            #print(strprime[:i], "for [:i]")
            #print(i,"is i")
            answer.append([strprime[i:],strprime[:i]])
            answer.append([strprime[:i],strprime[i:]])
            #print(answer, "is answer so far")
    return answer

#print(split(1097,listofprimes))
"""







"""def split(prime, listofprimes,integerform):
    answer = []
    lenprime = len(str(prime))
    strprime = str(prime)
    for i in range(1,lenprime):
        listsplit = [int(strprime[:i]), int(strprime[i:])]
        reverseprime = str(listsplit[1]) + str(listsplit[0])
        if ((listsplit[0] in listofprimes[:10**len(strprime[:i])]) 
            and (listsplit[1] in listofprimes[:10**len(strprime[i:])])
            and (int(reverseprime)) in listofprimes[:10**lenprime]):
            if int(reverseprime) > prime:
                if integerform:
                    answer.append([int(strprime[:i]),int(strprime[i:])])
                    answer.append([int(strprime[i:]),int(strprime[:i])])
                else:
                    answer.append([strprime[:i], strprime[i:]])
                    answer.append([strprime[i:],strprime[:i]])
    return answer"""

print(timeSieve)
print("--- %s seconds ---" % (time.time() - start_time))