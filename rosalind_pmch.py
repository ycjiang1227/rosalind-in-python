from math import factorial

sequence = input("Sequence: ")

# find number of Gs
num_G = 0
for n in range(0, len(sequence)):
    if sequence[n] == "G":
        num_G += 1

num_T = int((len(sequence) - (2*num_G))/2)

answer = factorial(num_G) * factorial(num_T)
print(answer)