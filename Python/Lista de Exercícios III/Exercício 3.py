#3. Supondo  que  a  população  de  um  país  A  seja  da  ordem  de  80000  habitantes  com  uma  taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários  para  que  a  população  do  país  A  ultrapasse  ou  iguale  a  população do  país  B, mantidas as taxas de crescimento 

A = 80000
B = 200000
anos = 0

while A <= B:
    A *= (1 + 0.03)
    B *= (1 + 0.015)
    anos += 1 
print(f"A população do país A ultrapassará a do país B em {anos} anos.")