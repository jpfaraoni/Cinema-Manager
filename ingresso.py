# Ingresso
# Atributos: sessão, assento, preço, status (disponível, vendido).
# Métodos: emitirIngresso(), cancelarIngresso(), verificarDisponibilidade().

from sessao import Sessao
from sala import Sala
from filme import Filme


class Ingresso:
    ingressos_db = []

    def __init__(self, sessao: Sessao, assento: str, preco: float, status: str = "disponível"):
        self.__sessao = sessao
        self.__assento = assento
        self.__preco = preco
        self.__status = status

    @property
    def sessao(self) -> Sessao:
        return self.__sessao

    @sessao.setter
    def sessao(self, sessao: Sessao):
        self.__sessao = sessao

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco


    def emitirIngresso(self):
        """Resumo das informações do ingresso comprado, caso o usuário esteja tentando comprar antes do início da sessão.
        As informações da sessão (com o filme, horário, preço).
        Aqui diminuiremos também o total de ingressos disponíveis.
        """
        pass

    def cancelarIngresso(self):
        """Cancelamento do ingresso vendido, caso o usuário esteja tentando cancelar antes do início da sessão.
        Retornará uma confirmação que o ingresso foi cancelado, com as a sala e nome do filme.
        """
        pass
