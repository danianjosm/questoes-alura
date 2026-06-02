#Modifique a classe Restaurante adicionando um construtor que aceita 
# nome e categoria como parâmetros e inicia ativo como False por padrão
# . Crie uma instância utilizando o construtor.

class Restaurante:

    def __init__(self, nome, categoria, ativo = False ):
        self.nome = nome 
        self.categoria = categoria 
        self.ativo = ativo 
       
    
restaurante_sabor = Restaurante("sabor de casa ", "brasileira")

restaurante_lacasa = Restaurante("la casa", "italiana")

print(vars(restaurante_sabor))
print(vars(restaurante_lacasa))