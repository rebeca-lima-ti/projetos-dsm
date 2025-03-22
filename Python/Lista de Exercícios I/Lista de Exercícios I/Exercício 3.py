dias = int(input("Digite a quantidade de dias:"))
hrs = int(input("Digite a quantidade de horas:"))
min = int(input("Digite a quantidade de minutos:"))
seg = int(input("Digite a quantidade de segundos:"))
hrs2 = dias*24+hrs
min2 = hrs2*60+min
seg2 = min2*60+seg
print(seg2)
