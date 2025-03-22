#6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$ 
# e. = Salário Liquido : R$

horas = float(input("Digite quantas horas você trabalha no mês: "))
money = float(input("Digite quanto você ganha por hora: "))

bruto = money * horas
imposto = bruto * 11 / 100
inss = bruto * 8 / 100
sind = bruto * 5 / 100
liquido = bruto - imposto - inss - sind

print(f"Salário bruto de R$ {bruto:.2f}.")
print(f"Valor pago ao IR: R$ {imposto:.2f}.")
print(f"Valor pago ao INSS: R$ {inss:.2f}.")
print(f"Valor pago ao Sindicato: R$ {sind:.2f}.")
print(f"Salário liquído de R$ {liquido:.2f}.")