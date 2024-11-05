import mysql.connector as sql

class SQL:
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
        self.conector = sql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        self.cursor = self.conector.cursor()

    def desconectar (self):
        
        self.cursor.close()
        self.conector.close()
        print('fechou')

    def listar_livros(self):
        
        self.cursor.execute('SELECT titulo, autor, genero, status, codigo FROM livro')
        
       
        resultados = self.cursor.fetchall()
        
        if not resultados:
            print("Nenhum livro encontrado.")
            return
        
        self.desconectar()
        
        
        for resultado in resultados:

            titulo, autor, genero, status, codigo = resultado
            print(f"Título: {titulo}, Autor: {autor}, Gênero: {genero}, Status: {status}, Código: {codigo}")

    def search(self, tituloS=None, autorS=None, generoS=None, statusS=None, codigoS=None):
        query = "SELECT titulo, autor, genero, status, codigo FROM livro WHERE 1=1"
    
        parametros = []

        if tituloS:
            query += " AND titulo LIKE %s"
            parametros.append('%' + tituloS.lower() + '%')
        
        if autorS:
            query += " AND autor LIKE %s"
            parametros.append('%' + autorS.lower() + '%')

        if generoS:
            query += " AND genero LIKE %s"
            parametros.append('%' + generoS.lower() + '%')

        if statusS:
            query += " AND status LIKE %s"
            parametros.append('%' + statusS.lower() + '%')

        if codigoS:
            query += " AND codigo = %s"
            parametros.append(codigoS)

        self.cursor.execute(query, parametros)
        resultados = self.cursor.fetchall()

        if resultados:
            for resultado in resultados:
                titulo, autor, genero, status, codigo = resultado
                print(f"Título: {titulo}, Autor: {autor}, Gênero: {genero}, Status: {status}, Código: {codigo}")
        else:
            print("Nenhum livro encontrado com os critérios fornecidos.")




class User:
    max_emprestimo = 3
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados = 0

class Livro:
    livros = []

    def __init__(self, titulo, autor, genero, status, codigo):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = status
        self.codigo = codigo
