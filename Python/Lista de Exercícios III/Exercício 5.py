#5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

while b != 0:
    a, b = b, a % b

print(f"O MDC é: {a}.")