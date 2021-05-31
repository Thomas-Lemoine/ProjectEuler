#problem 63
total = 0
for i in range(1,500):
    for j in range(1,500):
        if len(str(i ** j)) == j:
            total += 1

print(total)