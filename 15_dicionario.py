#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

comida= {"massa": "macarrão", "fruta": "maça", "carne": "bacon"}

verificar = input("Digite algo:")

if verificar in comida or verificar in comida.values():
    print(f"Nossa você acertou. {verificar} existe no dicionario")
else:
    print("vixi errou ein")
