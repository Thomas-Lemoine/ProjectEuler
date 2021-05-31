
f1 = 1
f2 = 1
index = 0
#while len(str(f1)) < 3:
while len(str(f1)) < 1000:
    f1, f2 = f2, f1+f2
    index += 1
print(index+1)

