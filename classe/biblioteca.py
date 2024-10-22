class User:
    max_emprestimo = 5
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados = 0

class Livro:
    livros = []

    def __init__(self, titulo, autor, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade
        Livro.livros.append(self)

    def listar_livros():
        if not Livro.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in Livro.livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Quantidade: {livro.quantidade}")

    def search(tituloS=None, autorS=None):
        encontrado = False
        for livro in Livro.livros:
            if (tituloS and tituloS.lower() in livro.titulo.lower()) or \
               (autorS and autorS.lower() in livro.autor.lower()):
                print(f'Título: {livro.titulo}\nAutor: {livro.autor}\nQuantidade: {livro.quantidade}')
                encontrado = True
        if not encontrado:
            print("Nenhum livro encontrado.")

    def emprestimo(usuario, titulo):
        for livro in Livro.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.quantidade > 0 and usuario.livros_emprestados < usuario.max_emprestimo:
                    livro.quantidade -= 1
                    usuario.livros_emprestados += 1
                    print(f"Empréstimo realizado com sucesso: '{livro.titulo}' para {usuario.nome}.")
                    return
                elif livro.quantidade == 0:
                    print(f'Desculpe, o livro "{livro.titulo}" não está disponível.')
                    return
                else:
                    print(f"{usuario.nome} já atingiu o limite de empréstimos.")
                    return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

livro1 = Livro(titulo="Dom Casmurro", autor="Machado de Assis", quantidade=3)
livro2 = Livro(titulo="1984", autor="George Orwell", quantidade=2)

print('='*30)

Livro.listar_livros()

print('='*30)

usuario1 = User("Alice", "123456789")
usuario2 = User("Elias", "123456789")

print(vars(usuario1))
print('='*30)

Livro.emprestimo(usuario1, "Dom Casmurro")
print('='*30)

print(vars(usuario1))
print('='*30)
Livro.listar_livros()
