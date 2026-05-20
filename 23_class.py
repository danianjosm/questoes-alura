#Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

class Restaurante:
    nome = ""
    categoria = ""
    ativo = False 
    
restaurante_praca = Restaurante ()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Italiana"

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

if restaurante_pizza.categoria == "Fast Food":
    print("Esse restaurante é Fast Food")
else:
    print("Esse restaurante não é Fast Food")
