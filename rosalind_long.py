import itertools

path = input("Folder Path: ")
with open(path) as data:
    data = data.read()
data = data.split(">")
data = [i.split("\n") for i in data]
data.pop(0)
data = [''.join(i[1:]) for i in data]

for result in itertools.pairwise(data):
    print("".join(result))

#solved