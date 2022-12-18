with open("/Users/yuchenjiang/Downloads/rosalind_cons (1).txt") as text_file:
    data = text_file.read()
data = data.split(">")
data = [i.split("\n") for i in data]
data.remove(data[0])
clean_data = [i[1:] for i in data]
dna_strings=[''.join(i) for i in clean_data]
profile = {"A": [], "C": [], "G": [], "T": []}
counter = []
consensus = []

print(len(dna_strings[0]))
for i in range(len(dna_strings[0])):
    for key in profile:
        profile[key].append(0)
    consensus.append(0)

def add_nt(n):
    for i in range(len(dna_strings[0])):
        for key in profile:
            if dna_strings[n][i] == key:
                    profile[key][i] += 1

def check_zero(i):
    count_zero = 0
    for key in profile:
        if profile[key][i] == 0:
            count_zero += 1
    if count_zero == 4:
        return True
    else:
        return False

for n in range(len(dna_strings)):
    add_nt(n)

# get final count

for i in range(len(dna_strings[0])):
    highest_count = 0
    for key in profile:
        if profile[key][i] > highest_count:
            # counter.append(profile[key][i])
            highest_count = profile[key][i]
    counter.append(highest_count)
    for key in profile:
        if profile[key][i] == highest_count:
            consensus[i] = key
    if check_zero(i):
        for key in profile:
            profile[key].pop(i)
consensus_seq = "".join(consensus)
# print(consensus)
print(consensus_seq)
for key in profile:
    print(f"{key}: {' '.join(str(i) for i in profile[key])}")


