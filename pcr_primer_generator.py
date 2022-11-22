seq_input = input("DNA sequence: ")
sequence = seq_input.upper()
# get reverse complement of sequence
revseq = sequence[::-1]

# get user inputted min / max Tm
min_tm = int(input("Minimum Tm : "))
max_tm = int(input("Maximum Tm: "))


# get complementary sequence of a given sequence
def get_comp(seq):
    result = []
    for nt in seq:
        if nt == "A":
            result.append("T")
        if nt == "G":
            result.append("C")
        if nt == "T":
            result.append("A")
        if nt == "C":
            result.append("G")
    result_string = "".join(result)
    return result_string


# calculate gc and tm for each primer
def gc_tm(primer):
    nt_counter = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
    for nt in primer:
        if nt in nt_counter:
            nt_counter[nt] += 1
        else:
            print("Invalid DNA sequence")
            quit
    gc_content = (nt_counter['G'] + nt_counter['C']) / len(primer) * 100
    tm = 81.5 + 0.41 * gc_content - 675 / (len(primer))
    return gc_content, tm


# generate list of primers 18-30 nt long
def primer_dict(seq):
    primer_list = []
    for n in range(18, 31):
        iter = seq[0:n]
        primer_list.append(iter)
    return primer_list


# check for g/c clamp at 3' end of primer
def check_clamp(primer):
    if primer[-1] == "G" or primer[-1] == "C":
        return True


# check for appropriate gc content between 40% and 60%
def gc_ok(gcvalue):
    if 40 <= gcvalue <= 60:
        return True


# check for appropriate tm between specified min_tm and max_tm
def tm_ok(tmvalue):
    if min_tm <= tmvalue <= max_tm:
        return True


seqcomp = get_comp(sequence)
revcomp = get_comp(revseq)

# store potential forward and reverse primers between length 18 and 30
fprimers = primer_dict(seqcomp)
rprimers = primer_dict(revcomp)

# generate pairs
pairs = []
for fkey in fprimers:
    for rkey in rprimers:
        iterpair = [fkey, rkey]
        pairs.append(iterpair)

# give scores to each pair of primers
for current_pair in pairs:
    pair_score = 0
    for n in range(0, 2):
        if check_clamp(current_pair[n]):
            pair_score += 1
        if gc_ok(gc_tm(current_pair[n])[0]):
            pair_score += 1
        if tm_ok(gc_tm(current_pair[n])[1]):
            pair_score += 1
    if -5 <= (gc_tm(current_pair[0])[1] - gc_tm(current_pair[1])[1]) <= 5:
        pair_score += 1
    current_pair.append(pair_score)

# sort pairs in descending order according to scores
sorted_pairs = sorted(pairs, key=lambda x: x[2], reverse=True)

# identify the highest score in among pairs
highest_score = 0
for pair in sorted_pairs:
    if pair[2] > highest_score:
        highest_score = pair[2]
# identify pairs with the highest scores
recommended_primers = []
for pair in sorted_pairs:
    if pair[2] == highest_score:
        recommended_primers.append([pair[0], pair[1]])

# print recommended primers
print("Recommended primers:")
for n in range(0, len(recommended_primers)):
    print(f'Pair {n + 1}:')
    print(f'Forward primer: {recommended_primers[n][0]}')
    print(f'Reverse primer: {recommended_primers[n][1]}')
