from filmecontrolador import FilmeControlador
from datetime import time

class FilmeVisao:
    def __init__(self):
        self.controlador = FilmeControlador()  # Instancia do controlador

    def tela_opcoes(self):
        print("-------- GERENCIAMENTO DE FILMES ----------")
        print("Escolha a opção:")
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
            print(f"Erro: {e}. Por favor, digite um número válido.")
            return self.tela_opcoes()  # Chama novamente para uma entrada correta

        return opcao

    from datetime import time

    def pega_dados_filme(self):
        """
        Solicita os dados de um filme ao usuário e retorna um dicionário com esses dados.
        """
        print("-------- DADOS DO FILME ----------")

        titulo = input("Título do filme: ")
        
        # Solicita a duração no formato HH:MM
        duracao_str = input("Duração do filme (HH:MM): ")
        try:
            horas, minutos = map(int, duracao_str.split(":"))
            duracao = time(horas, minutos)
        except ValueError:
            raise ValueError("Formato de duração inválido. Use HH:MM.")
        classificacao_etaria = int(input("Classificação etária do filme: "))
        
        return {
            "titulo": titulo,
            "duracao": duracao,
            "classificacao_etaria": classificacao_etaria
        }


    def mostra_filme(self, dados_filme):
        print("-------- FILME ----------")
        print(f"TÍTULO: {dados_filme.titulo}")
        print(f"DURAÇÃO: {dados_filme.duracao}")
        print(f"CLASSIFICAÇÃO: {dados_filme.classificacao_etaria}")
        print("\n")

    def seleciona_filme(self):
        try:
            titulo = input("Digite o título do filme que deseja selecionar: ")
        except ValueError:
            print("Erro: título inválido. Por favor, insira um título válido.")
            return self.seleciona_filme()  # Chama novamente para uma entrada correta

        return titulo

    def mostra_mensagem(self, msg):
        """
        Exibe uma mensagem para o usuário.
        """
        print(msg)

    def listar_filmes(self, filmes):
        if isinstance(filmes, str):  
            self.mostra_mensagem(filmes)
        else:
            if not filmes:  # Verifica se a lista de salas está vazia
                self.mostra_mensagem("Nenhum filme cadastrado.")
                return

            print("\nFilmes cadastrados:")
            for filme in filmes:
                self.mostra_filme(filme)
