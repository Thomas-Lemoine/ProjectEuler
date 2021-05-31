
#Problem 31

total = 200
ways = 1

#This is disgusting but hey, it works... heavily inspired from a link I lost.
for b in range(int(total/100) + 1):
    for c in range(int((total-b*100)/50) + 1):
        for d in range(int((total - b*100 - c*50)/20) + 1):
            for e in range(int((total - b*100 - c*50 - d*20)/10) + 1):
                for f in range(int((total - b*100 - c*50 - d*20 - e*10)/5) + 1):
                    for g in range(int((total - b*100 - c*50 - d*20 - e*10 - 5*f)/2) + 1):
                        for h in range(int(total - b*100 - c*50 - d*20 - e*10 - 5*f - 2*g) + 1):
                            if (b*100 + c*50 + d*20 + e*10 + f*5 + g*2 + h*1 == 200):
                                ways += 1
print(ways)