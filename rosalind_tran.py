s1 = input("s1: ")
s2 = input("s2: ")

num_transition = 0
num_transversion = 0

purines = ["A", "G"]
pyrimidines = ["T", "C"]
for n in range(0,len(s1)):

    if s1[n] == s2[n]:
        continue
    elif s1[n] in purines:
        if s2[n] in purines:
            num_transition += 1
        else:
            num_transversion += 1
    elif s1[n] in pyrimidines:
        if s2[n] in pyrimidines:
            num_transition += 1
        else:
            num_transversion += 1

ratio = num_transition / num_transversion
print(ratio)

