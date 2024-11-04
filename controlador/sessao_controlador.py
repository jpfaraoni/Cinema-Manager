from entidade.sessao import Sessao
from entidade.sessao import TipoSessao
from exception.sessao_nao_encontrada import SessaoNaoEncontrada
#from entidade import Ingresso
from datetime import datetime, timedelta
from exception.horario_invalido import HorarioInvalido
from visao.sessao_visao import SessaoVisao
from entidade.sessao import Sessao
from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from entidade.sala import Sala

class SessaoControlador(ControladorEntidadeAbstrata):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__sessoes_db = []
        self.__ingressos = []
        #ingressos = []
        self.__sessaovisao = SessaoVisao()


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

        for sessao in self.__sessoes_db:
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
            horario = dados_sessao["horario"]
            tipo = dados_sessao["tipo"]

            # Buscar o filme e a sala pelos dados fornecidos
            filme = self._controlador_sistema.filmecontrolador.busca_filme(dados_sessao["titulo"])
            sala = self._controlador_sistema.salacontrolador.busca_sala(dados_sessao["sala_numero"])

            # Validar as entradas
            if filme is None:
                self.__sessaovisao.mostra_mensagem("Erro: Filme não encontrado.")
                return

            if sala is None or not isinstance(sala, Sala):
                self.__sessaovisao.mostra_mensagem("Erro: Sala não encontrada ou tipo de sala inválido.")
                return

            if tipo is not None and not isinstance(tipo, TipoSessao):
                self.__sessaovisao.mostra_mensagem("Erro: Tipo de sessão inválido.")
                return

            # Validar o horário
            if not self.validar_horario(horario):
                raise HorarioInvalido(horario)

            # Criar uma nova sessão e verificar conflitos de horário
            nova_sessao = Sessao(filme, sala, horario, tipo)
            if not self.horario_disponivel(nova_sessao):
                self.__sessaovisao.mostra_mensagem(f"Erro: Conflito de horário na sala {sala.numero} para o horário {horario}.")
                return

            # Adicionar a sessão ao banco de dados
            self.__sessoes_db.append(nova_sessao)
            self.__sessaovisao.mostra_mensagem(f"Sessão do filme '{filme.titulo}' adicionada com sucesso!")

        except HorarioInvalido as e:
            self.__sessaovisao.mostra_mensagem(f"Erro: {e}")
        except ValueError as ve:
            self.__sessaovisao.mostra_mensagem(f"Erro de valor: {ve}")
        except Exception as ex:
            self.__sessaovisao.mostra_mensagem(f"Erro inesperado: {ex}")

    def atualizar_sessao(self):
        try:
            self.listar_sessoes()
            dados_sessao = self.__sessaovisao.seleciona_sessao()
            sessao = self.busca_sessao(dados_sessao["titulo"], dados_sessao["sala_numero"], dados_sessao["horario"])

            novos_dados_sessao = self.__sessaovisao.pega_novos_dados_sessao()
            nova_capacidade = novos_dados_sessao["capacidade"]
            novo_tipo = novos_dados_sessao["tipo"]

            if novos_dados_sessao is not None:
                if nova_capacidade is not None:
                    if nova_capacidade > 0:
                        sessao.sala.capacidade = nova_capacidade
                    else:
                        raise ValueError("Capacidade deve ser um valor positivo.")

                if novo_tipo is not None:
                    sessao.tipo = novo_tipo  # Atualiza o tipo

                return f"Sessão de {sessao.filme.titulo} atualizada com sucesso!"
        except SessaoNaoEncontrada as e:
            return str(e)

    def remover_sessao(self):
        #    def remover_sessao(self, filme, sala, horario):
        try:
            self.listar_sessoes()
            dados_sessao = self.__sessaovisao.seleciona_sessao()
            sessao = self.busca_sessao(dados_sessao["titulo"], dados_sessao["sala_numero"],
                                           dados_sessao["horario"])

            if (sessao is not None):
                self.__sessoes_db.remove(sessao)
                self.listar_sessoes()

        except SessaoNaoEncontrada as e:
            return str(e)

    def busca_sessao(self, filme_titulo: str, sala_numero: int, horario: str) -> Sessao:
        for sessao in self.__sessoes_db:
            if sessao.filme.titulo == filme_titulo and sessao.sala.numero == sala_numero and sessao.horario == horario:
                return sessao
        raise SessaoNaoEncontrada(filme_titulo, sala_numero, horario)

    def listar_sessoes(self):
        for e in self.__sessoes_db:
            ingressos_disponiveis = e.ingressos_disponiveis()
            self.__sessaovisao.mostra_sessao({"titulo": e.filme.titulo,
                                                    "numero_sala": e.sala.numero,
                                                    "horario": e.horario,
                                                    "tipo": e.tipo,
                                                    "ingressos_disponiveis": ingressos_disponiveis})

    def listar_ingressos(self):
        for e in self.__ingressos:
            self.__sessaovisao.mostra_ingressos({"titulo": e.filme.titulo,
                                                "numero_sala": e.sala.numero,
                                                "horario": e.horario,
                                                "tipo": e.tipo,})

    def relatorio_sessoes(self):
        """
        Método para gerar um relatório das sessões cadastradas.
        Por exemplo, mostra qual turno (manhã, tarde, noite) tem mais sessões.
        """
        turnos = {"manhã": 0, "tarde": 0, "noite": 0}

        for sessao in self.__sessoes_db:
            horario = datetime.strptime(sessao.horario, "%H:%M")
            if 6 <= horario.hour < 12:
                turnos["manhã"] += 1
            elif 12 <= horario.hour < 18:
                turnos["tarde"] += 1
            else:
                turnos["noite"] += 1


        if all(sessoes == 0 for sessoes in turnos.values()):
            self.__sessaovisao.mostra_mensagem("Nenhuma sessão cadastrada.")
        else:
            turno_mais_frequente = max(turnos, key=turnos.get)
            self.__sessaovisao.mostra_mensagem(
                f"O turno mais frequentado é: {turno_mais_frequente} com {turnos[turno_mais_frequente]} sessões."
            )



    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_sessao, 2: self.atualizar_sessao, 3: self.remover_sessao, 4: self.listar_sessoes,
                        5: self.listar_ingressos, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__sessaovisao.tela_opcoes()]()