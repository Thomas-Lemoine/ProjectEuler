
f = open('p022_names.txt','r')

message = f.read().replace('"', "")

#print(message)

lst = message.split(',')

#print(lst)

lst.sort()
score = 0

for i in range(len(lst)):
    total = 0
    for l in range(len(lst[i])):
        total += ord(lst[i][l]) - 64
    score += total * (i+1)   

print(score)
#871198282