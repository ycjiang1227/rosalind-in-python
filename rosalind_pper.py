import math

k = int(input("k: "))
n = int(input("n: "))

pper = math.factorial(n) / math.factorial(n-k)

answer = int(pper % 1000000)

print(answer)