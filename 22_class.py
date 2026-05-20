#Crie uma nova instância da classe Restaurante chamada 
# restaurante_pizza com o nome
# 'Pizza Place' e categoria 'Fast Food'.
class Restaurante():
    nome = ""
    categoria = ""
    ativo = False 
    
restaurante_praca = Restaurante()
restaurante_praca.categoria = "Italiana"
restaurante_praca.nome = "Praça"

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast food"

print(vars(restaurante_pizza))
