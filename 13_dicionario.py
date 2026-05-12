#2 - Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

dani = {"nome": "Dani", "idade": 19, "cidade": "Garanhuns", "faculdade": ""} # no dicionario existe chave e valor 

# modificando o valor da chave 
dani["cidade"] = "Recife" # muda o valor da chave 
print(dani)
#adicionando faculdade
dani["faculdade"] = input("digite o nome da sua faculdade: ")
print(dani)

if "cidade" in dani:
    del dani["cidade"]
print(f"apos a remoção da cidade {dani}")

#del dicionario["chave"]        # apaga simplesmente
#dicionario.pop("chave")        # apaga e devolve o valor
#dicionario.popitem()           # apaga o último par inserido
#dicionario.clear()         
