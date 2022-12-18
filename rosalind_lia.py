import math
k = 7
N = 37
P = 2**k
probability = 0
for i in range(N, P + 1):
    prob = (math.factorial(P) /
            (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(
                P - i))
    probability += prob
print(probability)