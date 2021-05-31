# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 08:54:07 2020

@author: thoma
"""

One = 3
Two = 3
Three = 5
Four = 4
Five = 4
Six = 3
Seven = 5
Eight = 5
Nine = 4
Ten = 3
Eleven = 6
Twelve = 6
Thirteen = 8
Fourteen = 8
Fifteen = 7
Sixteen = 7
Seventeen = 9
Eighteen = 8
Nineteen = 8
Twenty = 6
Thirty = 6
Forty = 5
Fifty = 5
Sixty = 5
Seventy = 7
Eighty = 6
Ninety = 6
HundredAnd = 10 
Hundred = 7
Thousand = 8



def NumLettersIn_n(n):
    total = 0
    #10 to 19
    if n % 100 == 10:
        total += Ten
    if n % 100 == 11:
        total += Eleven
    if n % 100 == 12:
        total += Twelve
    if n % 100 == 13:
        total += Thirteen
    if n % 100 == 14:
        total += Fourteen
    if n % 100 == 15:
        total += Fifteen
    if n % 100 == 16:
        total += Sixteen
    if n % 100 == 17:
        total += Seventeen
    if n % 100 == 18:
        total += Eighteen
    if n % 100 == 19:
        total += Nineteen
    #twenty to ninety
    if (n % 100 < 30) and (n % 100 >= 20):
        total += Twenty
    if (n % 100 < 40) and (n % 100 >= 30):
        total += Thirty
    if (n % 100 < 50) and (n % 100 >= 40):
        total += Forty
    if (n % 100 < 60) and (n % 100 >= 50):
        total += Fifty
    if (n % 100 < 70) and (n % 100 >= 60):
        total += Sixty
    if (n % 100 < 80) and (n % 100 >= 70):
        total += Seventy
    if (n % 100 < 90) and (n % 100 >= 80):
        total += Eighty
    if (n % 100 >= 90):
        total += Ninety
    #exactly 100, 200, 300, etc
    if n%1000 == 100:
        return One + Hundred
    if n%1000 == 200:
        return Two + Hundred
    if n%1000 == 300:
        return Three + Hundred
    if n%1000 == 400:
        return Four + Hundred
    if n%1000 == 500:
        return Five + Hundred
    if n%1000 == 600:
        return Six + Hundred
    if n%1000 == 700:
        return Seven + Hundred
    if n%1000 == 800:
        return Eight + Hundred
    if n%1000 == 900:
        return Nine + Hundred
    if n%100000 == 1000:
        return One + Thousand
    #Hundreds
    if (n%1000 >= 100):
        total += HundredAnd
    #two hundred to nine hundred
    if (n % 1000 < 200) and (n % 1000 >= 100):
        total += One
    if (n % 1000 < 300) and (n % 1000 >= 200):
        total += Two
    if (n % 1000 < 400) and (n % 1000 >= 300):
        total += Three
    if (n % 1000 < 500) and (n % 1000 >= 400):
        total += Four
    if (n % 1000 < 600) and (n % 1000 >= 500):
        total += Five
    if (n % 1000 < 700) and (n % 1000 >= 600):
        total += Six
    if (n % 1000 < 800) and (n % 1000 >= 700):
        total += Seven
    if (n % 1000 < 900) and (n % 1000 >= 800):
        total += Eight
    if (n % 1000 >= 900):
        total += Nine
    #1 to 9 if not 10 to 19
    if n%100 <= 9 or n%100 >= 20: 
        if n % 10 == 1:
            total += One
        if n % 10 == 2:
            total += Two
        if n % 10 == 3:
            total += Three
        if n % 10 == 4:
            total += Four
        if n % 10 == 5:
            total += Five
        if n % 10 == 6:
            total += Six
        if n % 10 == 7:
            total += Seven
        if n % 10 == 8:
            total += Eight
        if n % 10 == 9:
            total += Nine
    return total

def LongLettres(maximum):
    answer = 0
    for i in range(1,maximum+1):
        answer += NumLettersIn_n(i)
    return answer

#test
print(sum([NumLettersIn_n(n) for n in range(1,5+1)]))

print(LongLettres(1000))
    
        


