with open("/Users/yuchenjiang/Downloads/rosalind_grph (3).txt") as text_file:
    data = text_file.read()
data = data.split(">")
data = [i.split("\n") for i in data]
# print(data)
data.remove(data[0])
# print(data)
# dna_strings = [{i[0]: ''.join(i[1:])} for i in data]
dna_keys = [i[0] for i in data]
dna_strings = [''.join(i[1:]) for i in data]
edges = []

def check_match(suffix, t):
    target = t[:3]
    return suffix == target

# from dna_strings[i], get suffix substring of length k
for i in range(len(dna_strings)):
    check_seq = dna_strings[i][-3:]
# compare with prefix of other strings: strings[:k]
    for j in range(len(dna_strings)):
        if dna_strings[j] != dna_strings[i]:
            match = check_match(check_seq, dna_strings[j])
            if match:
                edges.append(dna_keys[i] + ' ' + dna_keys[j])

for i in edges:
    print(i)