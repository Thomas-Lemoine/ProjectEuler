
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse(n):
    return int(str(n)[::-1])

def Main():
    total = 0
    for x in range(1,10000):
        number = x
        i = 1
        while i <= 50:
            number = number + reverse(number)
            if is_palindrome(number):
                break
            if i == 50:
                total += 1
            i += 1
                
    print(total)
    
Main()