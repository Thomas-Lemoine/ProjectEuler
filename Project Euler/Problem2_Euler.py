
a = 0
b = 1
summ = 0
for x in range(1,1000):
    if a < 4000000:
        #print (a)
        a,b = b, a+b
        if a % 2 == 0:
            summ += a

print (f"The answer is : {summ}")
    
    
    