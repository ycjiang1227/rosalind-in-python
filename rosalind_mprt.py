# /Users/yuchenjiang/Downloads/rosalind_mprt.txt
import requests
import re

path = input("Folder Path: ")
with open(path, "r") as temp:
    seq_ids = [i.rstrip('\n') for i in temp]

# refine Uniprot IDs
# for n in range(0, len(seq_ids)):
#     position = seq_ids[n].find("_")
#     # remove all characters after "_", if any
#     if position != -1:
#         seq_ids[n] = seq_ids[n][0:position]

print(seq_ids)

sequences = {}

for n in range(0, len(seq_ids)):
    # refine uniprot id for requests
    position = seq_ids[n].find("_")
    if position != -1:
        # remove all characters after _ if any
        uniprot_id = seq_ids[n][0:position]
    else:
        uniprot_id = seq_ids[n]
    url = "http://www.uniprot.org/uniprot/" + uniprot_id + ".fasta"
    fasta_page = requests.get(url)
    fasta_decoded = fasta_page.text.split("\n")
    sequences[seq_ids[n]] = ["".join(fasta_decoded[1:])]

print(sequences)

for uniprot_id in sequences:
    n_positions = []
    # identify all indices of appearance of N and add to list n_positions
    n_object = re.finditer(pattern="N", string=sequences[uniprot_id][0])
    for index in n_object:
        n_positions.append(index.start())
    # check motif for
    for i in n_positions:
        if (sequences[uniprot_id][0][i + 1] != "P"
                and (sequences[uniprot_id][0][i + 2] == "S"
                     or sequences[uniprot_id][0][i + 2] == "T")
                and sequences[uniprot_id][0][i + 1] != "P"):
            sequences[uniprot_id].append(str(i + 1))

for n in sequences:
    if len(sequences[n]) != 1:
        print(n)
        glyc_positions = " ".join(sequences[n][1:])
        print(glyc_positions)
