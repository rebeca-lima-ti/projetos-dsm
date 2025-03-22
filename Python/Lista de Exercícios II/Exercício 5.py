#5. Faça um Programa que leia três números e mostre o maior e o menor deles.

valor1 = float(input("Entre com o primeiro valor: "))
valor2 = float(input("Entre com o segundo valor: "))
valor3 = float(input("Entre com o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3: #primeiro valor
    if valor2 > valor3:
        print(f"O primeiro valor {valor1} é o maior e o terceiro valor {valor3} é o menor!")
    elif valor2 == valor3:
        print(f"O primeiro valor {valor1} é o maior e os valores restantes ({valor2}) são menores!")
    else:
        print(f"O primeiro valor {valor1} é o maior e o segundo valor {valor2} é o menor!")
elif valor2 > valor1 and valor2 > valor3: #segundo valor
    if valor1 > valor3:
        print(f"O segundo valor {valor2} é o maior e o terceiro valor {valor3} é o menor!")
    elif valor1 == valor3:
        print(f"O segundo valor {valor2} é o maior e os valores restantes ({valor1}) são menores!")
    else:
        print(f"O segundo valor {valor2} é o maior e o primeiro valor {valor1} é o menor!")
elif valor3 > valor1 and valor3 > valor2: # terceiro valor
    if valor1 > valor2:
        print(f"O terceiro valor {valor3} é o maior e o segundo valor {valor2} é o menor!")
    elif valor1 == valor2:
        print(f"O terceiro valor {valor3} é o maior e os valores restantes ({valor1}) são menores!")
    else:
        print(f"O terceiro valor {valor3} é o maior e o primeiro valor {valor1} é o menor!")