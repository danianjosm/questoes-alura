#Altere o valor do atributo nome para 'Bistrô'.

class Restaurante():
    nome = ""
    categoria = ""
    ativo = False 
    
restaurante_praca = Restaurante()
restaurante_praca.categoria = "Italiana"
restaurante_praca.nome = "Praça"

# alterar o objeto 

restaurante_praca.nome = "Bistrô"
print(restaurante_praca.nome)