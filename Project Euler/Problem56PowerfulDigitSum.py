def sum_digits(n):
    sumtot = 0
    for digit in str(n):
        sumtot += int(digit)
    return sumtot

maxSumDigits = 0
for a in range(1,100):
    for b in range(1,100):
        number = a ** b
        sumdigitsN = sum_digits(number)
        if sumdigitsN > maxSumDigits:
            maxSumDigits = sumdigitsN
            permA = a
            permB = b
print(f"{maxSumDigits} is the answer!")
print(permA)
print(permB)