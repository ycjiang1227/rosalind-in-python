# list all nums
# list of groupings
# for each grouping

with open("/Users/yuchenjiang/Downloads/rosalind_tree (2).txt", "r") as temp:
    data = [i.rstrip('\n') for i in temp]

n = int(data[0])
print(n)
pairs = [list(i.split(" ")) for i in data[1:]]


int_pairs = []
for i in pairs:
    j = [int(k) for k in i]
    int_pairs.append(j)

print(int_pairs)

print(n - len(int_pairs) -1)

#solved