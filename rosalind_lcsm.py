from datetime import datetime
startTime = datetime.now()
with open("/Users/yuchenjiang/Downloads/rosalind_lcsm (3).txt") as text_file:
    data = text_file.read()
data = data.split(">")
data = [i.split("\n") for i in data]
data.remove(data[0])
clean_data = [i[1:] for i in data]
dna_strings = [''.join(i) for i in clean_data]

def present_in_all(substring):
    counter = 0
    for i in dna_strings:
        if substring in i:
            counter += 1
    if counter == len(dna_strings):
        return True
    else:
        return False

lcs = ''

for start in range(len(dna_strings[0])):
    cont = True
    for length in range(len(dna_strings[0])):
        if cont:
            check_string = dna_strings[0][start:start+length+1]
            if present_in_all(check_string):
                if len(check_string) >= len(lcs):
                    lcs = check_string
            else:
                cont = False

print(lcs)
print(datetime.now() - startTime)
