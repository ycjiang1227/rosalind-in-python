# /Users/yuchenjiang/Downloads/rosalind_revp.txt
path = input("Folder Path: ")
with open(path, "r") as temp:
    sequence = [i.rstrip('\n') for i in temp]
    sequence.pop(0)
    sequence = "".join(sequence)


# create reverse complement of sequence
def create_revcomp(seq):
    revcomp = []
    for nt in seq:
        if nt == "A":
            revcomp.insert(0, "T")
        if nt == "T":
            revcomp.insert(0, "A")
        if nt == "C":
            revcomp.insert(0, "G")
        if nt == "G":
            revcomp.insert(0, "C")
    revcomp = "".join(revcomp)
    return revcomp


revcomp_seq = create_revcomp(sequence)

palindromes = []
for n in range(len(sequence)):
    for length in range(4, 13):
        # check all possible strings between 4 and 12 nt long
        if (n + length) > len(sequence):
            break
        check_sequence = sequence[n:n + length]
        check_revcomp = revcomp_seq[len(sequence) - n - length: len(sequence) - n]
        if check_sequence == check_revcomp:
            palindromes.append(f"{n + 1} {length}")

for n in palindromes:
    print(n)
