#4. Faça um Programa que leia três números e mostre o maior deles.

valor1 = float(input("Entre com o primeiro valor: "))
valor2 = float(input("Entre com o segundo valor: "))
valor3 = float(input("Entre com o terceiro valor: "))

if valor1 >= valor2 and valor1 >= valor3:
    print(valor1, "é o maior!")
elif valor2 >= valor1 and valor2 >= valor3:
    print(valor2, "é o maior!")
else:
    print(valor3, "é o maior!")