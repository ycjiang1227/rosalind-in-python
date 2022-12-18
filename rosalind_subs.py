s = input("string s: ")
t = input("substring t: ")

def check_t(string, n):
    current = s[n:n+len(t)]
    if current == t:
        return True

positions = []
for n in range(len(s)):
    if check_t(s, n):
        positions.append(str(n+1))
print(" ".join(positions))
