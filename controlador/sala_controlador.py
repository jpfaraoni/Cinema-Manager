from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from entidade.sala import Sala
from exception.sala_nao_encontrada import SalaNaoEncontrada
from visao.sala_visao import SalaVisao

class SalaControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__salas_db = []
        self.__salavisao = SalaVisao()


    def adicionar_sala(self):
        try:
            dados_sala = self.__salavisao.pega_dados_sala()
            numero = dados_sala["numero"]
            capacidade = dados_sala["capacidade"]
            if capacidade <= 0:
                raise ValueError(f"Capacidade precisa ser positiva")

            for sala in self.__salas_db:
                if sala.numero == numero:
                    raise ValueError(f"Sala {numero} já está cadastrada.")

            nova_sala = Sala(numero, capacidade)
            self.__salas_db.append(nova_sala)
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
                raise Exception(f"Capacidade deve ser positivo.")
            else:
                sala.capacidade = nova_capacidade

            self.__salavisao.mostra_mensagem(f"Sala {numero} atualizada com sucesso!")
        except SalaNaoEncontrada as e:
            self.__salavisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__salavisao.mostra_mensagem(f"Erro inesperado: {e}")

    def busca_sala(self, numero):
        for sala in self.__salas_db:
            if sala.numero == numero:
                return sala
        raise SalaNaoEncontrada(numero)

    def remover_sala(self):
        try:
            self.lista_salas()
            numero = self.__salavisao.seleciona_sala()
            sala = self.busca_sala(numero)

            self.__salas_db.remove(sala)
            self.__salavisao.mostra_mensagem(f"Sala {numero} foi removida com sucesso.")
        except SalaNaoEncontrada as e:
            self.__salavisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__salavisao.mostra_mensagem(f"Erro inesperado: {e}")

    def lista_salas(self):
        if not self.__salas_db:
            self.__salavisao.mostra_mensagem("Nenhuma sala cadastrada.")
            return

        salas_info = [{"numero": sala.numero, "capacidade": sala.capacidade} for sala in self.__salas_db]
        self.__salavisao.exibe_lista_salas(salas_info)

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_sala, 2: self.atualizar_sala, 3: self.remover_sala, 4: self.lista_salas, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__salavisao.tela_opcoes()]()

