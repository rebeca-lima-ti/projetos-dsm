salario = float(input("Digite seu salário:"))
porcent = float(input("Digite o aumento em porcentagem:"))
aumento = salario*porcent/100
novo = salario+aumento
print(f"Novo salário: R${novo:.2f}.")
print(f"Aumento: R${aumento:.2f}.")
