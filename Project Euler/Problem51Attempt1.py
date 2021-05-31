#Problem51

def isPrime(n):
    if (n == 2):
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    for i in range(3,int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True



def insertchar(LongNum,index1,index2,char):
    StrNum = str(LongNum)
    strchar = char
    if index2 < len(StrNum):
        return StrNum[:index1] + strchar + StrNum[index1:index2] + strchar + StrNum[index2:]
    else:
        return StrNum[:index1] + strchar + StrNum[index1:] + strchar
                   
#print(insertchar(123456789, 5, 12, 1))
#print(len(str(123456789)))


def Main():
    maxi = 0
    answer = ""
    num = 0
    while maxi < 8:
        num += 1
        lennum = len(str(num))
        for pos1 in range(0,lennum+1):
            for pos2 in range(pos1,lennum+2):
                total = 0
                for char in range(0,10):
                    if (isPrime(int(insertchar(num, pos1, pos2, str(char)))) and not (char == 0 and pos1 == 0)):
                        total += 1                        
                if total > maxi:
                    maxi = total
                    print(int(insertchar(num, pos1, pos2, str(char))))
                    for x in range(0,10):
                        if isPrime(int(insertchar(num, pos1, pos2, str(x)))):
                            answer = insertchar(num, pos1, pos2, str(x))
                            answer1 = insertchar(num, pos1, pos2, "*")
                            pos1perm = pos1
                            pos2perm = pos2
                            charperm = x
                            break
    print(maxi, "primes")
    print(answer, "is the number (with the 2 numbers added")
    print(answer1)
    print(charperm, "is the lowest number for replacing")
    print(pos1perm, "is the first position")
    print(pos2perm, "is the second position")
    

Main()
#Ahhhhhhhhhhhh