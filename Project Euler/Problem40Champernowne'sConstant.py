
number = ""
answer = 1
for integer in range(1,1000000):
    number = number + str(integer)
for i in range(len(str(1000000))):
    answer *= int(number[10**i - 1])
print(answer)
