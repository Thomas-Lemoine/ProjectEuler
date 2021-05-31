#Problem 59 : XOR decryption

f = open('cipher.txt','r')
chartest = str(f)
for char in f:
    lst = char.split(',')


def cypher(message,password):
    lst = []
    for char in message:
        lst.append(char)
    count = 0
    while count < len(lst):
        for i in range(len(password)):
            a = ord(lst[count])
            a ^= ord(password[i])
            lst[count] = a
            count += 1
    return lst
        

def decrypt(lst,password):
    count = 0
    while count < len(lst):
        for i in range(len(password)):
            a = int(lst[count])
            a ^= ord(password[i])
            lst[count] = a
            count += 1
    message = ""
    for element in lst:
        message += chr(element)
    return message

#We found the password, "exp"

message = decrypt(lst,"exp")
print(message)


#count the sum of ASCII codes
lstordmess = []
for i in range(len(message)):
    lstordmess.append(message[i])
ans = 0
for element in lstordmess:
    ans = ans + ord(element)
print(f"{ans} is the answer!")