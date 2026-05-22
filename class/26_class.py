#Crie uma classe chamada Restaurante com os atributos 
# nome, categoria, ativo e crie mais 2 atributos. 
# Instancie um restaurante e atribua valores aos seus
#  atributos.

class Restaurante:

    def __init__(self, nome, categoria, ativo, vegano, cidade):
        self.nome = nome
        self.categoria = categoria 
        self.ativo = ativo 
        self.vegano = vegano 
        self.cidade = cidade 

    
restaurante_sabor = Restaurante("sabor de casa ", "brasileira", True, False, "Recife")

restaurante_lacasa = Restaurante("la casa", "italiana", True, True, "olinda")

print(vars(restaurante_sabor))