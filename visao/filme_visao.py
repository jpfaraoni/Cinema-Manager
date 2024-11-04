class FilmeVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- GERENCIAMENTO DE FILMES ----------")
        print("1 - Adicionar Filme")
        print("2 - Atualizar Filme")
        print("3 - Remover Filme")
        print("4 - Listar Filmes")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha a opção: "))
            if opcao not in [0, 1, 2, 3, 4]:
                raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}")
            return self.tela_opcoes()

        return opcao

    def pega_dados_filme(self):
        print("-------- DADOS DO FILME ----------")
        try:
            titulo = input("Título do filme: ")

            duracao = int(input("Duração do filme(em minutos): "))
            if duracao <= 0:
                raise ValueError

            genero = input("Digite o genero: ")
            # Verifica se o gênero contém apenas letras e espaços
            if not all(c.isalpha() or c.isspace() for c in genero):
                raise ValueError("O gênero deve conter apenas letras e espaços.")

            classificacao_etaria = int(input("Classificação etária do filme: "))
            if classificacao_etaria < 0:
                raise ValueError

            return {
                "titulo": titulo,
                "duracao": duracao,
                "genero": genero,
                "classificacao_etaria": classificacao_etaria
            }
        except ValueError:
            raise ValueError("Dados inválidos.")

    def pega_novos_dados_filme(self):
        try:
            duracao = int(input("Nova duração do filme(em minutos): "))
            if duracao <= 0:
                raise ValueError

            genero = input("Novo gênero do filme: ")
            # Verifica se o gênero contém apenas letras e espaços
            if not all(c.isalpha() or c.isspace() for c in genero):
                raise ValueError("O gênero deve conter apenas letras e espaços.")

            classificacao_etaria = int(input("Nova classificação etária do filme: "))
            if classificacao_etaria < 0:
                raise ValueError

            return {
                "duracao": duracao,
                "genero": genero,
                "classificacao_etaria": classificacao_etaria
            }
        except ValueError:
            raise ValueError("Dados inválidos.")

    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_filme(self):
        titulo = input("Digite o título do filme que deseja selecionar: ")
        return titulo

    def listar_filmes(self, filmes):
        if not filmes:
            self.mostra_mensagem("Nenhum filme cadastrado.")
            return

        print("\nFilmes cadastrados:")
        for filme in filmes:
            print(f"TÍTULO: {filme['titulo']}, DURAÇÃO: {filme['duracao']}, GÊNERO: {filme['genero']}, CLASSIFICAÇÃO: {filme['classificacao_etaria']}")

