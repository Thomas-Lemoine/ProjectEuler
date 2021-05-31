
def checkForDigitCancelling(numer,denom):
    strNumer = str(numer)
    strDenom = str(denom)
    taille = len(strNumer)
    for i in range(0,taille):
        if ((int(strDenom[taille-1-i]))>0) and ((strNumer[1] == strDenom[0]) or (strNumer[0] == strDenom[1])) and ((int(strNumer[i]))/(int(strDenom[taille-1-i])) == numer/denom):
            return True
    return False
  
lst = []          
checkForDigitCancelling(22, 99)
for secondnum in range(10,100):
    for firstnum in range(10,secondnum):
        if checkForDigitCancelling(firstnum, secondnum) and ((firstnum*secondnum) % 11 != 0):
            print(str(firstnum) + " and " + str(secondnum))

"""answer and explanation :
Solutions : 
16 and 64
26 and 65
19 and 95
49 and 98

Which equate to : 
1/4
2/5
1/5
1/2

If we multiply them together, we get 1/100. The denominator is 100, which is the answer."""