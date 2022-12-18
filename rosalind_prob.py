from math import log
s = input("s: ")
a = input("A: ")
array = a.split(" ")

GC_count = 0
for nt in s:
    if nt == "G" or nt == "C":
        GC_count += 1
AT_count = len(s) - GC_count

b = []
for k in array:
    GC_prob = float(k) / 2
    AT_prob = (1-float(k))/2
    b_k = log((GC_prob ** GC_count * AT_prob ** AT_count), 10)
    b.append(str(b_k))

result = " ".join(b)
print(result)