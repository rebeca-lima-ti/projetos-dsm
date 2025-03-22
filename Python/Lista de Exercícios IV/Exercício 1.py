#1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.

import random
numlist = random.sample(range(1, 101), 10)

maior = menor = numlist[0]
x = 0
while x < 10:
    if numlist[x] > maior: 
        maior = numlist[x]
    elif numlist[x] < menor:
        menor = numlist[x]
    x += 1

print ("Números:", numlist)
print (f"O maior número é: {maior}")
print (f"O menor número é: {menor}")