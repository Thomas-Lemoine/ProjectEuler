
for a in range(1,100):
    for b in range(1,100):
        First = (a ** 2)-(b ** 2)
        Second = 2*a*b
        Third = a ** 2 + b ** 2
        if First > 0 and First + Second + Third == 1000:
            print(First * Second * Third)
            