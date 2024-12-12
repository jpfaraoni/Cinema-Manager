from entidade.filme import Filme
from exception.filme_nao_encontrado import FilmeNaoEncontrado
from visao.filme_visao import FilmeVisao
from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from DAO.filme_dao import FilmeDAO

class FilmeControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__filmevisao = FilmeVisao()
        self.__filme_DAO = FilmeDAO()

    def adicionar_filme(self):
        try:
            dados_filme = self.__filmevisao.pega_dados_filme()
            if dados_filme is None:
                return
            titulo = dados_filme["titulo"]
            duracao = dados_filme["duracao"]

            if not isinstance(duracao, int):
                raise ValueError("Duração deve ser em minutos.")

            try:
                self.busca_filme(titulo)  # Tenta buscar o filme pelo título
                raise Exception(f"Filme '{titulo}' já está cadastrado.")
            except FilmeNaoEncontrado:
                novo_filme = Filme(
                    dados_filme["titulo"],
                    dados_filme["duracao"],
                    dados_filme["genero"],
                    dados_filme["classificacao_etaria"]
                )
                # USO DE DAO PARA SERIALIZAÇÃO
                self.__filme_DAO.add(novo_filme)
                self.__filmevisao.mostra_mensagem(f"Filme '{titulo}' foi adicionado com sucesso!")

        except ValueError as ve:
            self.__filmevisao.mostra_mensagem(f"Erro: {ve}")
        except Exception as e:
            self.__filmevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def atualizar_filme(self):
        #TODO implementar um metodo update na classe DAO abstrata e realizar o update apos atualizar o objeto para o db refletir a nova instancia.
        try:
            self.listar_filmes()
            titulo = self.__filmevisao.seleciona_filme()
            if titulo is None:
                return
            filme = self.busca_filme(titulo)

            novos_dados = self.__filmevisao.pega_novos_dados_filme()
            if novos_dados is None:
                return
            filme.duracao = novos_dados["duracao"]
            filme.genero = novos_dados["genero"]
            filme.classificacao_etaria = novos_dados["classificacao_etaria"]

            self.__filme_DAO.update(filme)
            self.listar_filmes()

            self.__filmevisao.mostra_mensagem(f"Filme '{titulo}' atualizado com sucesso!")
        except ValueError as ve:
            self.__filmevisao.mostra_mensagem(f"Erro: {ve}")
        except FilmeNaoEncontrado as e:
            self.__filmevisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__filmevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def busca_filme(self, titulo):
        filmes = self.__filme_DAO.get_all()
        for filme in filmes:
            if filme.titulo == titulo:
                return filme
        raise FilmeNaoEncontrado(titulo)

    def remover_filme(self):
        try:
            self.listar_filmes()
            titulo = self.__filmevisao.seleciona_filme()
            if titulo is None:
                return
            filme = self.busca_filme(titulo)

            # USO DE DAO PARA SERIALIZACAO
            self.__filme_DAO.remove(titulo)
            self.__filmevisao.mostra_mensagem(f"Filme '{titulo}' foi removido com sucesso.")
        except FilmeNaoEncontrado as e:
            self.__filmevisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__filmevisao.mostra_mensagem(f"Erro inesperado: {e}")

    #SERIALIZACAO USANDO DAO
    def listar_filmes(self):
        filmes = self.__filme_DAO.get_all()
        if not filmes:
            self.__filmevisao.mostra_mensagem("Nenhum filme cadastrado.")
            return
        filmes_info = [{"titulo": filme.titulo, "duracao": filme.duracao, "genero": filme.genero,
                        "classificacao_etaria": filme.classificacao_etaria} for filme in filmes]
        self.__filmevisao.listar_filmes(filmes_info)

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_filme, 2: self.atualizar_filme, 3: self.remover_filme, 4: self.listar_filmes, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__filmevisao.tela_opcoes()]()
