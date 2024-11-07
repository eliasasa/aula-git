import db
from connect import config

class Livro:
    sql = db.SQL(**config)
    livros = []
    def __init__(self, titulo, autor, genero, status, codigo):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = status
        self.codigo = codigo
    
    def create ():
        query = 'INSERT INTO livro(titulo, autor, genero, status, codigo) values(%s, %s, %s, %s, %s)'

        tituloA = str(input('Título: '))
        autorA = str(input('Autor: '))
        generoA = str(input('Genero: '))
        codigoA = str(input('Código: '))

        create = Livro.sql.cursor.execute(query, (tituloA, autorA, generoA, 'Disponível', codigoA))
        print("Livro adicionado com sucesso!")
        return create #mandar para outra classe livrocontroler
