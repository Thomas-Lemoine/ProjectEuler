num = 1
#7830457
for i in range(7830457):
    num *= 2
    strnum = str(num)
    if len(strnum) > 10:
        num = int(strnum[-10:])
enddigits = int(str(28433*num + 1)[-10:])
print(enddigits)