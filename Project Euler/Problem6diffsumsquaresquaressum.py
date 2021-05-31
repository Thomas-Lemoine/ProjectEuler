
""" The sum of the squares of the first ten natural numbers is,
1^2 + 2^2  + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1+2+3+4+5...+10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum."""

def SumOfSquares(n):
    answer = 0
    for x in range(1,n+1):
        answer += (x ** 2)
    return answer

def SquareOfSum(n):
    temp = 0
    for x in range(1,n+1):
        temp += x
    return (temp ** 2)

def differenceSoS(n):
    print(SquareOfSum(n) - SumOfSquares(n))
    
    
differenceSoS(100)