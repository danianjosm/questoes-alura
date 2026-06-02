#Crie uma classe chamada Restaurante com os atributos nome, categoria,
# ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    
    restaurante = []

    def __init__(self, nome, categoria, ativo, cidade, vegano):
        
        self.nome = nome
        self.categoria = categoria 
        self.ativo = ativo
        self.cidade = cidade 
        self.vegano = vegano 
        Restaurante.restaurante.append(self)



restaurante_pizza = Restaurante("Pizzaria lá casa", "Italiana", True, "Recife", False)
restaurante_ama = Restaurante("AMA", "Comida caseira", True, "Olinda", True)

for individual in Restaurante.restaurante:
    print(individual.nome, "|", individual.categoria, "|", individual.ativo, "|", individual.cidade, "|", individual.vegano )