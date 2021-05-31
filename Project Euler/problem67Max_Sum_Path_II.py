import time
f = open("p067_triangle.txt", 'r')
data = f.read().splitlines()
for lineind in range(len(data)):
    data[lineind] = [int(num) for num in data[lineind].split()]

data = data[::-1]
for levelind in range(len(data) - 1):
    for numberind in range(len(data[levelind]) - 1):
        if data[levelind][numberind] > data[levelind][numberind + 1]:
            data[levelind + 1][numberind] += data[levelind][numberind]
        else:
            data[levelind + 1][numberind] += data[levelind][numberind + 1]
        
print(data[-1][0])

        

