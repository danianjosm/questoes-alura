# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida,
#  instancie 3 objetos desta classe e atribua valores aos seus atributos 
# através de um método construtor.

class Cliente:
    def __init__(self, nome, idade, genero, cadastro_ativo = False):
        self.nome = nome 
        self.idade = idade 
        self.genero = genero
        self.cadastro_ativo = cadastro_ativo

    def __str__(self):
       return f"o cliente {self.nome} do genero {self.genero} está como cadastro {self.cadastro_ativo}"

client1 = Cliente ("Raissa", 32, "feminino", cadastro_ativo = True)
cliente2 = Cliente ("Carlos", 67, "masculino")
cliente3 = Cliente ("Fernanda", 18, "feminino")

print(client1)