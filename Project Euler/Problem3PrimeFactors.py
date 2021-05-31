

def primeFactors(n):
    prime_factors_lst = []
    while n % 2 == 0: 
        prime_factors_lst.append(2)
        n /= 2
    for i in range(3,n-1,2): 
        while n % i== 0: 
            prime_factors_lst.append(i)
            n /= i 
    if n > 2: 
        prime_factors_lst.append(i)

primeFactors(60085)

