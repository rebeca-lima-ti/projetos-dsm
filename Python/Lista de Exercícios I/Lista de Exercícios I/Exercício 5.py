prod = float(input("Digite o preço do produto:"))
porcent = float(input("Digite o desconto em porcentagem:"))
desc = prod*porcent/100
preco = prod-desc
print(f"O preço a pagar é: R${preco:.2f}.")
print(f"Desconto: R${desc:.2f}.")
