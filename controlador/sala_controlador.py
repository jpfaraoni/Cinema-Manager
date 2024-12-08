from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from entidade.sala import Sala
from exception.sala_nao_encontrada import SalaNaoEncontrada
from visao.sala_visao import SalaVisao
from DAO.saladao import SalaDAO

class SalaControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__salas_db = []
        self.__salavisao = SalaVisao()
        self.__sala_DAO = SalaDAO()


    def adicionar_sala(self):
        try:
            dados_sala = self.__salavisao.pega_dados_sala()
            if dados_sala is not None:
                numero = dados_sala["numero"]
                capacidade = dados_sala["capacidade"]

                if capacidade <= 0:
                    raise ValueError(f"Capacidade precisa ser positiva")

                try:
                    self.busca_sala(numero)  # Tenta buscar o filme pelo título
                    raise Exception(f"Sala {numero} já está cadastrada.")
                except SalaNaoEncontrada:
                    nova_sala = Sala(dados_sala["numero"],dados_sala["capacidade"])
                    # USO DE DAO PARA SERIALIZAÇÃO
                    self.__sala_DAO.add(nova_sala)
                    self.__salavisao.mostra_mensagem(f"Sala {numero} foi adicionada com sucesso!")
        except ValueError as ve:
            self.__salavisao.mostra_mensagem(f"Erro: {ve}")
        except Exception as e:
            self.__salavisao.mostra_mensagem(f"Erro inesperado: {e}")

    def atualizar_sala(self):
        try:
            self.lista_salas()
            numero = self.__salavisao.seleciona_sala()
            sala = self.busca_sala(numero)

            nova_capacidade = self.__salavisao.pega_novos_dados_sala()
            if nova_capacidade <= 0:
                raise ValueError(f"Capacidade deve ser um valor positivo.")
            if nova_capacidade is not None:
                sala.capacidade = nova_capacidade

            self.__sala_DAO.update(sala)
            self.lista_salas()
            # self.__salavisao.mostra_mensagem(f"Sala {numero} atualizada com sucesso!")
        except SalaNaoEncontrada as e:
            self.__salavisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__salavisao.mostra_mensagem(f"Erro inesperado: {e}")

    def busca_sala(self, numero):
        salas = self.__sala_DAO.get_all()
        for sala in salas:
            if sala.numero == numero:
                return sala
        raise SalaNaoEncontrada(numero)

    def remover_sala(self):
        try:
            self.lista_salas()
            numero = self.__salavisao.seleciona_sala()
            sala = self.busca_sala(numero)

            self.__sala_DAO.remove(sala)
            self.__salavisao.mostra_mensagem(f"Sala {numero} foi removida com sucesso.")
        except SalaNaoEncontrada as e:
            self.__salavisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__salavisao.mostra_mensagem(f"Erro inesperado: {e}")

    def lista_salas(self):
        salas = self.__sala_DAO.get_all()
        if not salas:
            self.__salavisao.mostra_mensagem("Nenhuma sala cadastrada.")
            return
        salas_info = [{"numero": sala.numero, "capacidade": sala.capacidade} for sala in salas]
        self.__salavisao.exibe_lista_salas(salas_info)

    # def listar_filmes(self):
    #     filmes = self.__filme_DAO.get_all()
    #     # if not filmes:
    #     #     self.__filmevisao.mostra_mensagem("Nenhum filme cadastrado.")
    #     filmes_info = [{"titulo": filme.titulo, "duracao": filme.duracao, "genero": filme.genero,
    #                     "classificacao_etaria": filme.classificacao_etaria} for filme in filmes]
    #     self.__filmevisao.listar_filmes(filmes_info)

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_sala, 2: self.atualizar_sala, 3: self.remover_sala, 4: self.lista_salas, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__salavisao.tela_opcoes()]()

