from itertools import product

symbols = input("Alphabet: ")
n = int(input("n: "))

alphabet = symbols.split(" ")

strings = ["".join(result) for result in product(alphabet, repeat=n)]

for i in strings:
    print(i)
