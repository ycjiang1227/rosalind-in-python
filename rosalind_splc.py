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
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '', 'TAG': '',
    'TGC': 'C', 'TGT': 'C', 'TGA': '', 'TGG': 'W',
}

# process file into list of strings
path = input("Folder Path: ")
with open(path) as data:
    data = data.read()
data = data.split(">")
data = [i.split("\n") for i in data]
data.pop(0)
data = [''.join(i[1:]) for i in data]

# obtain DNA string s
s = data[0]

# obtain introns and sort by descending length
introns = data[1:]
introns.sort(key=len, reverse=True)

# remove introns from sequence, obtain only exon
for intron in introns:
    s = s.replace(intron, "")

# split exon into codons
s_codons = [s[i:i + 3] for i in range(0, len(s), 3)]

# get amino acid sequence
protein_string = []
for codon in s_codons:
    for triplet in genetic_code:
        if codon == triplet:
            protein_string.append(genetic_code[triplet])

print("".join(protein_string))
