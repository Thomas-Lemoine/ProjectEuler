# -*- coding: utf-8 -*-
import time as t
    
def isPalindrome(number):
    return (str(number) == str(number)[::-1])
    
def HighestPalindromicProduct(digits):
    answer = 0
    Palindrome = []
    #check for all numbers from 100 to 999
    for First in range(10 ** (digits - 1), 10 ** digits):
        for Second in range(10 ** (digits - 1), 10 ** digits):
            temp = First * Second
            """ if the answer is a palindrome and is bigger than the previous biggest
            one found, that's your answer"""
            if isPalindrome(temp):
                Palindrome.append(temp)
    answer = max(Palindrome)
    print(answer)

#invoking the function
t0 = t.time()
HighestPalindromicProduct(2)
t1 = t.time()
print(t1-t0)