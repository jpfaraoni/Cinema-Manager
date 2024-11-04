from entidade.filme import Filme
from exception.filmenaoencontrado import FilmeNaoEncontrado
from visao.filmevisao import FilmeVisao
from controlador.controlador_entidade_abstrata import ControladorEntidadeAbstrata

class FilmeControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__filmes_db = []
        self.__filmevisao = FilmeVisao()


    def adicionar_filme(self):
        try:
            dados_filme = self.__filmevisao.pega_dados_filme()
            titulo = dados_filme["titulo"]
            duracao = dados_filme["duracao"]

            # if not isinstance(duracao, int):
            #     raise ValueError("Duração deve ser em minutos.")

            # Verifica se o filme já está cadastrado
            for filme in self.__filmes_db:
                if filme.titulo == titulo:
                    raise ValueError(f"Filme '{titulo}' já está cadastrado.")

            novo_filme = Filme(dados_filme["titulo"], dados_filme["duracao"], dados_filme["genero"], dados_filme["classificacao_etaria"])
            self.__filmes_db.append(novo_filme)
            self.__filmevisao.mostra_mensagem(f"Filme '{titulo}' foi adicionado com sucesso!")

        except ValueError as e:
            self.__filmevisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__filmevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def atualizar_filme(self):
        try:
            self.listar_filmes()
            titulo = self.__filmevisao.seleciona_filme()
            filme = self.busca_filme(titulo)

            novos_dados = self.__filmevisao.pega_novos_dados_filme()
            filme.duracao = novos_dados["duracao"]
            filme.genero = novos_dados["genero"]
            filme.classificacao_etaria = novos_dados["classificacao_etaria"]

            self.__filmevisao.mostra_mensagem(f"Filme '{titulo}' atualizado com sucesso!")
        except FilmeNaoEncontrado as e:
            self.__filmevisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__filmevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def busca_filme(self, titulo):
        for filme in self.__filmes_db:
            if filme.titulo == titulo:
                return filme
        raise FilmeNaoEncontrado(titulo)

    def remover_filme(self):
        try:
            self.listar_filmes()
            titulo = self.__filmevisao.seleciona_filme()
            filme = self.busca_filme(titulo)

            self.__filmes_db.remove(filme)
            self.__filmevisao.mostra_mensagem(f"Filme '{titulo}' foi removido com sucesso.")
        except FilmeNaoEncontrado as e:
            self.__filmevisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__filmevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def listar_filmes(self):
        if not self.__filmes_db:
            self.__filmevisao.mostra_mensagem("Nenhum filme cadastrado.")
            return

        filmes_info = [{"titulo": filme.titulo, "duracao": filme.duracao, "genero": filme.genero, "classificacao_etaria": filme.classificacao_etaria} for filme in self.__filmes_db]
        self.__filmevisao.listar_filmes(filmes_info)

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_filme, 2: self.atualizar_filme, 3: self.remover_filme, 4: self.listar_filmes, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__filmevisao.tela_opcoes()]() #teste
