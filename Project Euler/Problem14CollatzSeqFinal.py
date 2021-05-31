# -*- coding: utf-8 -*-

def CollatzSeq(Start):
    #si even divide by 2
    n = Start
    chainLength = 1
    while (n != 1):
        if (n % 2 == 0):
            n = n/2
        else:
            n = 3*n + 1
        chainLength += 1
    Answer = []
    Answer.append(chainLength)
    Answer.append(Start)
    return Answer

Sequence = 0
Initial = 0
for i in range(1,1000000):
    if CollatzSeq(i)[0] > Sequence:
        Sequence = CollatzSeq(i)[0]
        Initial = CollatzSeq(i)[1]
print(Initial, ":", Sequence)


