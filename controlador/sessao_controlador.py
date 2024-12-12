from exception.filme_nao_encontrado import FilmeNaoEncontrado
from exception.sala_nao_encontrada import SalaNaoEncontrada
from exception.sessao_nao_encontrada import SessaoNaoEncontrada
from datetime import datetime, timedelta
from exception.horario_invalido import HorarioInvalido
from visao.sessao_visao import SessaoVisao
from entidade.sessao import Sessao
from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from random import randint
from DAO.sessao_dao import SessaoDAO


class SessaoControlador(ControladorEntidadeAbstrata):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__sessoes_db = []
        self.__ingressos = []
        self.__sessaovisao = SessaoVisao()
        self.__sessao_DAO = SessaoDAO()

        """
        Controlador responsável por gerenciar as Sessões.

        Atributos:
        - sessoes_db: Simula o banco de dados emr memória para as sessões.
        """

    def horario_disponivel(self, nova_sessao: Sessao):
        """
        Verifica se há conflito entre o horário da nova sessão e as sessões já cadastradas,
        calculando o horário de término da sessão ao mesmo tempo.
        """
        # Valida o horário da nova sessão
        if not self.validar_horario(nova_sessao.horario):
            raise HorarioInvalido(nova_sessao.horario)

        novo_horario_inicio = datetime.strptime(nova_sessao.horario, "%H:%M")
        novo_horario_termino = novo_horario_inicio + timedelta(minutes=int(nova_sessao.filme.duracao))

        sessoes = self.__sessao_DAO.get_all()
        for sessao in sessoes:
            if sessao.sala.numero == nova_sessao.sala.numero:
                horario_inicio_existente = datetime.strptime(sessao.horario, "%H:%M")
                horario_termino_existente = horario_inicio_existente + timedelta(minutes=int(sessao.filme.duracao))

                # Verifica se há sobreposição de horários entre as sessões
                if (novo_horario_inicio < horario_termino_existente and
                        novo_horario_termino > horario_inicio_existente):
                    return False  # Conflito de horário
        return True  # Horário disponível

    def validar_horario(self, horario):
        """
        Valida se o horário está no formato HH:MM.
        Retorna True se o horário for válido, caso contrário, False.
        """
        try:
            datetime.strptime(horario, "%H:%M")
            return True
        except ValueError:
            return False

    def adicionar_sessao(self):
        try:
            # Listar filmes e salas para auxiliar o usuário na escolha
            self._controlador_sistema.filmecontrolador.listar_filmes()
            self._controlador_sistema.salacontrolador.lista_salas()

            # Obter dados da sessão a partir da visão
            dados_sessao = self.__sessaovisao.pega_dados_sessao()
            if dados_sessao is not None:
                horario = dados_sessao["horario"]
                tipo = dados_sessao["tipo"]

                # Buscar o filme e a sala pelos dados fornecidos
                filme = self._controlador_sistema.filmecontrolador.busca_filme(dados_sessao["titulo"])
                sala = self._controlador_sistema.salacontrolador.busca_sala(dados_sessao["sala_numero"])

                # Validar o horário
                if not self.validar_horario(horario):
                    raise HorarioInvalido(horario)

                # Criar uma nova sessão e verificar conflitos de horário
                nova_sessao = Sessao(filme, sala, horario, randint(0, 10000), tipo)
                if not self.horario_disponivel(nova_sessao):
                    raise Exception(f"Erro: Conflito de horário na sala {sala.numero} para o horário {horario}.")

                # Adicionar a sessão ao banco de dados
                self.__sessao_DAO.add(nova_sessao)
                self.__sessaovisao.mostra_mensagem(f"Sessão do filme '{filme.titulo}' adicionada com sucesso!")

        except HorarioInvalido as e:
            self.__sessaovisao.mostra_mensagem(f"Erro: {e}")
        except FilmeNaoEncontrado as fne:
            self.__sessaovisao.mostra_mensagem(fne)
        except SalaNaoEncontrada as sne:
            self.__sessaovisao.mostra_mensagem(sne)
        except ValueError as ve:
            self.__sessaovisao.mostra_mensagem(f"Erro: {ve}")
        except Exception as ex:
            self.__sessaovisao.mostra_mensagem(f"Erro inesperado: {ex}")

    def atualizar_sessao(self):
        try:
            self.listar_sessoes()
            codigo = self.__sessaovisao.seleciona_sessao()
            if codigo is None:
                return
            sessao = self.busca_sessao(codigo)

            novos_dados_sessao = self.__sessaovisao.pega_dados_sessao()
            if novos_dados_sessao is None:
                return
            filme = self._controlador_sistema.filmecontrolador.busca_filme(novos_dados_sessao["titulo"])
            sala = self._controlador_sistema.salacontrolador.busca_sala(novos_dados_sessao["sala_numero"])
            horario = novos_dados_sessao["horario"]
            novo_tipo = novos_dados_sessao["tipo"]

            if not self.validar_horario(horario):
                raise HorarioInvalido(horario)

            if novos_dados_sessao is not None:
                sessao.filme = filme
                sessao.sala = sala
                sessao.horario = horario
                sessao.tipo = novo_tipo

                self.__sessao_DAO.update(sessao)
                self.listar_sessoes()
                self.__sessaovisao.mostra_mensagem(f"Sessão de {sessao.filme.titulo} atualizada com sucesso!")
        except FilmeNaoEncontrado as fne:
            self.__sessaovisao.mostra_mensagem(fne)
        except SalaNaoEncontrada as sne:
            self.__sessaovisao.mostra_mensagem(sne)
        except ValueError as ve:
            self.__sessaovisao.mostra_mensagem(f"Erro de valor: {ve}")
        except Exception as ex:
            self.__sessaovisao.mostra_mensagem(f"Erro inesperado: {ex}")

    def remover_sessao(self):
        #    def remover_sessao(self, filme, sala, horario):
        try:
            self.listar_sessoes()
            codigo = self.__sessaovisao.seleciona_sessao()
            if codigo is None:
                return
            sessao = self.busca_sessao(codigo)
            self.__sessao_DAO.remove(codigo)
            self.listar_sessoes()
        except SessaoNaoEncontrada as sne:
            self.__sessaovisao.mostra_mensagem(sne)
        except ValueError as ve:
            self.__sessaovisao.mostra_mensagem(ve)

    def busca_sessao(self, codigo: int):
        sessoes = self.__sessao_DAO.get_all()
        for sessao in sessoes:
            if sessao.codigo == codigo:
                return sessao
        raise SessaoNaoEncontrada(codigo)

    def listar_sessoes(self):
        sessoes = self.__sessao_DAO.get_all()
        if not sessoes:
            self.__sessaovisao.mostra_mensagem("Nenhuma sessão cadastrada.")
        for sessao in sessoes:
            ingressos_disponiveis = sessao.ingressos_disponiveis
            self.__sessaovisao.mostra_sessao({"titulo": sessao.filme.titulo,
                                              "numero_sala": sessao.sala.numero,
                                              "horario": sessao.horario,
                                              "codigo": sessao.codigo,
                                              "tipo": sessao.tipo,
                                              "ingressos_disponiveis": ingressos_disponiveis})

    def relatorio_sessoes(self):
        """
        Método para gerar um relatório das sessões cadastradas.
        Por exemplo, mostra qual turno (manhã, tarde, noite) tem mais sessões.
        """
        turnos = {"manhã": 0, "tarde": 0, "noite": 0}
        sessoes = self.__sessao_DAO.get_all()
        for sessao in sessoes:
            horario = datetime.strptime(sessao.horario, "%H:%M")
            if 6 <= horario.hour < 12:
                turnos["manhã"] += 1
            elif 12 <= horario.hour < 18:
                turnos["tarde"] += 1
            else:
                turnos["noite"] += 1

        if all(turnos_sessoes == 0 for turnos_sessoes in turnos.values()):
            self.__sessaovisao.mostra_mensagem("Nenhuma sessão cadastrada.")
        else:
            turno_mais_frequente = max(turnos, key=turnos.get)
            self.__sessaovisao.mostra_mensagem(
                f"O turno com mais sessões é: {turno_mais_frequente} com {turnos[turno_mais_frequente]} sessões."
            )

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_sessao, 2: self.atualizar_sessao, 3: self.remover_sessao,
                        4: self.listar_sessoes, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__sessaovisao.tela_opcoes()]()
