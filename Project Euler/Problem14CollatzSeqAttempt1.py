# -*- coding: utf-8 -*-


def CollatzSeq(Start):
    #si even divide by 2
    n = Start
    chainLength = 1
    while (n != 1) and chainLength < 100:
        if (n % 2 == 0):
            n = n/2
        else:
            n = 3*n + 1
        chainLength += 1
        print(chainLength)
        print(n)
    Answer = []
    Answer.append(chainLength)
    Answer.append(Start)
    return Answer

for i in range(0,100):
    Final = 0
    Initial = 0
    if CollatzSeq(i)[0] > Final:
        Final = CollatzSeq(i)[0]
        Initial = CollatzSeq(i)[1]

#print(Initial, ":", Final)
print(CollatzSeq(13))

    

        
        