# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:16:05 2020

@author: thoma
"""

def isDivisibleBy(divided, divisor):
    return (divided % divisor == 0)
def isLeap(year):
    if isDivisibleBy(year, 100):
        return (isDivisibleBy(year, 400))
    return isDivisibleBy(year, 4)
def isSunday(i):
    return (i % 7 == 6)
        
def isFirstOfMonth():
    year = 1901
    lst = [0]
    day = 0
    regmonth = 31
    while year < 2000:
        
        #Jan:
        day += 31
        lst.append(day)
        #feb:
        if isLeap(year):
            day += 29
            lst.append(day)
        else:
            day += 28
            lst.append(day)
        #march
        day += regmonth
        lst.append(day)
        #april
        day += 30
        lst.append(day)
        #may
        day += regmonth
        lst.append(day)
        #June
        day += 30
        lst.append(day)
        #July
        day += regmonth
        lst.append(day)
        #August
        day += regmonth
        lst.append(day)
        #September
        day += 30
        lst.append(day)
        #October
        day += regmonth
        lst.append(day)
        #November
        day += 30
        lst.append(day)
        #December
        day += regmonth
        lst.append(day)
        year += 1
    return lst

totalSundays = 0
for i in isFirstOfMonth():
    if isSunday(i):
        totalSundays += 1

print(totalSundays)
