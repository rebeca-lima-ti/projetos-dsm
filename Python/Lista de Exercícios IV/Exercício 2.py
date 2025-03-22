#2. Sorteie  20  inteiros  entre  1  e  100  numa  lista.  Armazene  os  números  pares  na  lista  PAR  e  os números ímpares na lista IMPAR. Imprima as três listas.

import random
numlist = random.sample(range(1, 101), 10)
par = []
impar = []

for x in numlist:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print(f"Lista completa: {numlist}")
print(f"Lista de pares: {par}")
print(f"Lista de impares: {impar}")