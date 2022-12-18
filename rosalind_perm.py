n = int(input("n: "))

from itertools import permutations

numbers = []
for i in range(n):
    numbers.append(i+1)
perm = list(permutations(numbers))
combi = [' '.join(map(str,i)) for i in perm]
print(len(combi))
for i in combi:
    print(i)