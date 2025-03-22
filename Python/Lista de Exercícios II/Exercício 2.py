#2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

year = int(input("Digite um ano: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Bissexto.")
else:
    print("Não é bissexto.")