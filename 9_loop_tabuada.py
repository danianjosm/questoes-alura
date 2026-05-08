#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10. // tive dificuldade de pensar na logica 

numero = int(input("Digite um numero para obter a tabuada: "))

for i in range (1,11):
    resultado = numero * i 
    print(f"{resultado}")
    