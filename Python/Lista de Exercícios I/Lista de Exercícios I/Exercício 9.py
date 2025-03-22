kmperc = float(input("Digite a quantidade de km percorridos:"))
dias = int(input("Digite a quantidade de dias inteiros pelos quais o carro foi alugado:"))
precokm = kmperc*0.15
precodias = dias*60
print(f"Valor total a pagar: R${precokm+precodias:.2f}.")