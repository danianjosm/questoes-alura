#Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

 
class Restaurante():
    nome = ""
    categoria = ""
    ativo = False 
    
restaurante_praca = Restaurante()
restaurante_praca.categoria = "Italiana"
restaurante_praca.nome = "Praça"

if restaurante_praca.ativo == False:
    print("O restaurante esta inativo")
else:
    print("O restaurante esta ativo")