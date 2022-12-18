import re

genetic_code = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}

path = input("Folder Path: ")
with open(path,"r") as temp:
    sequence = [i.rstrip('\n') for i in temp]
    sequence.pop(0)
    sequence = "".join(sequence)

# create list of indices of start codons
def find_starts(seq):
    start_positions = []
    start_object = re.finditer(pattern='ATG', string=seq)
    for index in start_object:
        start_positions.append(index.start())
    return start_positions


# create list of indices of stop codons
def find_stops(seq):
    stop_positions = []
    stoplist = ["TAA", "TAG", "TGA"]
    for codon in stoplist:
        stop_object = re.finditer(pattern=codon, string=seq)
        for index in stop_object:
            stop_positions.append(index.start())
    stop_positions.sort()
    return stop_positions


# turn a nucleotide sequence into an amino acid sequence
def dna_to_protein(seq):
    seq_codons = [seq[i:i + 3] for i in range(0, len(seq), 3)]
    protein = []
    for codon in seq_codons:
        for i in genetic_code:
            if codon == i:
                protein.append(genetic_code[i])
    protein = "".join(protein)
    return protein


# if stop and start codon are in frame with each other, translate sequence into amino acid sequence and add to list
def find_prots(starts,stops,seq):
    prots = []
    for start in starts:
        for stop in stops:
            if (stop > start) and ((stop-start)%3 == 0):
                orf = seq[start:stop]
                protein = dna_to_protein(orf)
                prots.append(protein)
                break
    return prots

# create reverse complement of sequence
revcomp = []
for nt in sequence:
    if nt == "A":
        revcomp.insert(0,"T")
    if nt == "T":
        revcomp.insert(0,"A")
    if nt == "C":
        revcomp.insert(0,"G")
    if nt == "G":
        revcomp.insert(0,"C")
revcomp = "".join(revcomp)

# generate proteins reading from 5' to 3' direction
forward_starts = find_starts(sequence)
forward_stops = find_stops(sequence)
forward_prots = find_prots(forward_starts, forward_stops,sequence)

# generate proteins reading from 3' to 5' direction
reverse_starts = find_starts(revcomp)
reverse_stops = find_stops(revcomp)
reverse_prots = find_prots(reverse_starts, reverse_stops,revcomp)

# combine and print proteins, removing any duplicates
all_prots = forward_prots + reverse_prots
all_prots = list(dict.fromkeys(all_prots))
for prot in all_prots:
    print(prot)

