# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
 
class Restaurante():
    nome = ""
    categoria = ""
    tipo = False 
    
restaurante_praca = Restaurante()
restaurante_praca.categoria = "Italiana"
restaurante_praca.nome = "Praça"

print(restaurante_praca.nome)