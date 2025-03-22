#3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor  de  20  elementos, cujos valores  deverão  ser  compostos  pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.

import random
numlist = random.sample(range(1, 101), 10)
numlist2 = random.sample(range(1, 101), 10)
numlist3 = []

x = 0
while x < 10:
    numlist3.append(numlist[x])
    numlist3.append(numlist2[x])
    x += 1

print(f"Primeira lista: {numlist}")
print(f"Primeira lista: {numlist2}")
print(f"Primeira lista: {numlist3}")