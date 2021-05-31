rangee = 100
mylist = []
for a in range(2, rangee + 1):
    for b in range(2,rangee + 1):
        mylist.append(a**b)
print(len(list(set(mylist))))