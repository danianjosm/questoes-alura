#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo 
        self.cor = cor 
        self.ano = ano 
        Carro.carros.append(self)

    def __str__(self):
        return f"{self.modelo} | {self.cor}"
    
    def __int__(self):
        return int(self.ano)
    
    def listar_carros():
        for carro in Carro.carros:
            print(f"{carro.modelo} | {carro.cor} | {carro.ano}")
    
carro_fiat = Carro ("fiat uno", "cinza", 2000 )
carro_jeep = Carro ("compass", "verde" , 2020)

Carro.listar_carros()

