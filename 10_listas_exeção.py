#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções. 
# /// n aprendi de fato esse tryexeption try:
    # código que pode dar erro
# except TipoDoErro:
    # o que fazer se der esse erro eu tambem erro e coloco =+

numeros= [1,4,5,7,9,"casa", 3,4,5]
soma = 0 

for i in numeros:
    try:
        soma += i 
        print(f"{soma}")
    except TypeError:
        pass 
