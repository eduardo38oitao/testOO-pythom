class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite




conta = Conta(535,"Ricardo",55.0)
conta1 = Conta(115,"Ana",515.0,2000.0)
print(conta)
print(conta1)



class Video:
    def __init__(self, titulo, tempo, views):
        self.titulo = titulo
        self.tempo = tempo
        self.views = views
    

video = Video("edu, agua e fogo", 1.2, 101010)

class Livro:
    def __init__(self,titulo,autor,data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao

livro = Livro("dudu","carlos",2020-11-29)