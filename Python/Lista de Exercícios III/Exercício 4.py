#4. A  seqüência  de  Fibonacci  é  a  seguinte:  1,  1,  2,  3,  5,  8,  13,  21,  34,  55,  ...  Sua  regra  de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

num = int(input("Digite o número de Fibonacci a ser calculado: "))

a, b = 1, 1

if num == 1 or num == 2:
    print(f"O {num}º número de Fibonacci é: 1.")
else:
    x = 3
    while x <= num:
        a, b = b, a + b
        x += 1
    print(f"O {num}º número de Fibonacci é: {b}.")