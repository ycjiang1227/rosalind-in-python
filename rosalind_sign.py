import itertools

n = int(input("n: "))

integers = list(range(1,n+1))

all_perm = []
for i in itertools.permutations(integers):
    for j in itertools.product([-1, 1], repeat = n):
        perm = [i[0]*i[1] for i in list(zip(i,j))]
        all_perm.append(perm)

print(len(all_perm))
for i in all_perm:
    print(*i, sep=" ")

#solved