#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
quantidade_de_palavras = {}
frase = input("Digite uma frase: ")
palavras = frase.split() # .split quebra a frase em palavras
print(palavras)

for n in palavras:
    if n in quantidade_de_palavras: # para cada palavra 
        quantidade_de_palavras[n] = quantidade_de_palavras[n] + 1 
    else:
        quantidade_de_palavras[n] = 1

print(quantidade_de_palavras)

