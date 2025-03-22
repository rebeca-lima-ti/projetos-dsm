#7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

area = float(input("Digite em metros o tamanho da área a ser pintada: "))

if area % 54 == 0:
  latas = area/54
else:
  latas = int(area/54)+1
  
preco = latas*80

print(f"Serão necessárias {latas} latas.")
print(f"O total a ser pago é: R${preco:.2f}.")