#Adicione um método de instância chamado emprestar à classe Livro que
#  define o atributo disponivel como False. Crie uma instância da classe,
#  chame o método 
# emprestar e imprima se o livro está disponível ou não. como eu faço 
# isso me ensine

class Livro:
    def __init__(self,titulo, autor, ano_publicado):
        self.titulo = titulo 
        self.autor = autor 
        self.ano_publicado = ano_publicado
        self.disponivel = True
    

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano_publicado}"
    def emprestar(self):
        self.disponivel = False
        return f"não disponivel"

livro1 = Livro("pequeno principe", "Antoine de Saint ", 1943) 
livro2 = Livro("bom dia veronica", "Rafael montes", 2022)

print(livro1.disponivel)

livro1.emprestar() 
print(livro1.disponivel)