# Sessão
# Atributos: filme, sala, horário, data, ingressosDisponíveis.
# Métodos: criarSessão(), atualizarSessão(), cancelarSessão().

from filme import Filme
from sala import Sala


class Sessao:
    sessoes_db = []

    def __init__(self, filme: Filme, sala: Sala, horario, ingressos_disponiveis):
        self.__filme = filme
        self.__sala = sala
        self.__horario = horario
        self.__ingressos_disponiveis = ingressos_disponiveis

    @property
    def filme(self) -> Filme:
        return self.__filme

    @filme.setter
    def filme(self, filme: filme):
        self.__filme = filme

    @property
    def sala(self) -> Sala:
        return self.__sala

    @sala.setter
    def sala(self, sala: Sala):
        self.__sala = sala

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: str):
        self.__horario = horario

    def adicionarSessao(self):
        """
        Aqui iremos adicionar a sessão a uma lista de sessões para podermos utilizar essa lista posteriormente.
        Retorna uma confirmação: "Sessão da sala: (número da sala) às (horárioda sessão) foi adicionada com sucesso!"
        """

    def atualizarSessao(self, filme=None, sala=None, data=None, ingressos_disponiveis=None):
        """
        Método para atualizar os atributos de uma sessão, caso as informações sejam passadas corretamente (não forem Null).
        Retorna os novos atributos.
        """

    def removerSessao(self):
        """
        Método para remover uma sessão do sistema, caso a sessão que queremos excluir esteja cadastrada.
        Retorna a confirmação com a sessão exluída, caso esta seja encontrada.
        Retorna "Sessão do filme: (nome do filme) não encontrada" caso a sessão fornecida não esteja na lista de sessões.
        """
