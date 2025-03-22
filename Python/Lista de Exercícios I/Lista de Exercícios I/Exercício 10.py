cig = int(input("Digite a quantidade de cigarros inteiros que você fuma por dia:"))
anos = int(input("Digite a quantos anos você fuma:"))
totalcig = 365*anos*cig
min = totalcig*10
totaldias = min/1440
print(f'O total de dias perdidos é: {totaldias:.1f}.')