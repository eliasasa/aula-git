import mysql.connector as sql
#from biblioteca import User, Livro

conector = sql.connect (
    host='10.28.2.62',
    user='suporte',
    password='suporte',
    database='biblioteca'
)

cursor = conector.cursor()

#cursor.execute('insert into livro (titulo, autor, genero, status, codigo) values ("O Pequeno Principe", "Enzo", "Fantasia", "Disponivel", 123);')
cursor.execute('INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES ("A Menina que Roubava Livros", "Markus Zusak", "Drama", "Disponível", 124);')
cursor.execute('INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES ("1984", "George Orwell", "Distopia", "Disponível", 125);')
cursor.execute('INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES ("O Hobbit", "J.R.R. Tolkien", "Fantasia", "Disponível", 126);')
cursor.execute('INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES ("O Alquimista", "Paulo Coelho", "Ficção", "Disponível", 127);')
cursor.execute('INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", "Disponível", 128);')

# Não se esqueça de fazer commit se necessário
conector.commit()

cursor.execute('select * from livro;')
x = cursor.fetchall()

print(x)

conector.commit()