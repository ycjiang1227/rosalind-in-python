n = int(input("months: "))
m = int(input("lifespan: "))

rabbits = [1, 1]
months = 2

while months < n:
    if months < m:
        rabbits.append(rabbits[-2] + rabbits [-1])
    elif months == m + 1 or months == m:
        rabbits.append(rabbits[-2] + rabbits[-1] - 1)
    else:
        rabbits.append(rabbits[-2] + rabbits[-1] - rabbits[-(m + 1)])
    months +=1
print(rabbits[-1])


