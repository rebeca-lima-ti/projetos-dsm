#1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print ("Não é um triângulo!")
elif lado1 == lado2 == lado3:
    print("Equilátero!")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Isósceles!")
else:
    print("Escaleno!")