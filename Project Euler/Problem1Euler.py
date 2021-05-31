def answer(n):
    answer = sum([x for x in range(1,n) if (x%3==0) or (x%5==0)])
    print(f"The sum is {answer}")

answer(1000)