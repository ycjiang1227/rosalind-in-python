# /Users/yuchenjiang/Downloads/Rosalind_sseq.txt
path = input("Folder Path: ")
with open(path) as data:
    data = data.read()
data = data.split(">")
data = [i.split("\n") for i in data]
data.pop(0)
data = [''.join(i[1:]) for i in data]

# obtain s and t
s = data[0]
t = data[1]
indices = []

pos = 0

for i in range(len(t)):
    for j in range(pos, len(s)):
        pos += 1
        if t[i] == s[j]:
            indices.append(pos)
            break
print(*indices)

#solved