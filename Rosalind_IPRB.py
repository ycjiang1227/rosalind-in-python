from math import comb
k = int(input("k: "))
m = int(input("m: "))
n = int(input("n: "))

population = k + m + n
pairs = comb(population,2)
offspring_pop = pairs * 4

dom_offspring = (comb(k,2) * 4) + (m * n * 4) + (n * k * 4) + (comb(m,2) * 3 ) + (n * m * 2)

probability = dom_offspring / offspring_pop
print(probability)