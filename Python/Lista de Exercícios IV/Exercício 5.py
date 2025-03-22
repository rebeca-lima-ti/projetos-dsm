#5. Seja  o  mesmo  texto  acima  “splitado”.  Calcule  quantas  palavras  possuem  uma  das  letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais. 

text = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.".lower()
text = text.replace(",","")
text = text.replace(":","")
text = text.replace(".","")

textlist = text.split(sep=" ")

def letras(palavra):
    for x in palavra:
        if x in 'python':
            return True
    return False

lista = []
for y in textlist:
    if letras(y) and len(y) > 4:
        lista.append(y)

print(lista)
print(len(lista))