import itertools

a = input("alphabet: ")
n = int(input("n: "))

alphabet = a.replace(" ","")


all_strings = []
for i in range(1, n+1):
    for result in itertools.product(alphabet, repeat = i):
        all_strings.append("".join(result))


order = sorted(all_strings, key = lambda word: [alphabet.index(c) for c in word] )

for i in order:
    print(i)

#solved