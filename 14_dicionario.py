#3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

print("Você vera os quadrados do 5 primeiros numeros")
 
numero ={} #dicionario
for n in range(1,6): 
    numero[n] = n**2

print(numero)