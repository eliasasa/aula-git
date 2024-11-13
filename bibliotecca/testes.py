import mysql.connector as sql
from config.db import SQL
from controllers.biblioteca import Biblioteca
from models.livro import Livro

# db = SQL(host='10.28.2.62', user='suporte', password='suporte', database='biblioteca')

# Inserir livros no banco de dados (comentado, pois você já inseriu)
# db.cursor.execute('insert into livro (titulo, autor, genero, status, codigo) values ("O Pequeno Principe 2", "Enzo", "Fantasia", "Disponivel", 125);')
# cursor.execute('INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES ("A Menina que Roubava Livros", "Markus Zusak", "Drama", "Disponível", 124);')

# db.conector.commit()

# db.cursor.execute('SELECT * FROM livro')
# resultados = db.cursor.fetchall()

# db.listar_livros()

# db.search(autorS='Enzo')
# db.search()

# for resultado in resultados:
#     print(resultado)

# for i in x:
#     titulo, autor, genero, status, codigo = i
#     Livro(titulo=titulo, autor=autor, genero=genero, status=status, codigo=codigo)

# print(Livro.livros)


# livro_exemplo = Livro.livros[0]  
# livro_exemplo.listar_livros()  


# livro_exemplo.search(autorS='Enzo')

# conector.commit()


# Biblioteca.search(autorS='Enzo', codigoS=123)

# Biblioteca.listar_livros()

# Livro.add_livro()

Biblioteca.add_livro()