from entidade.cliente import Cliente
from entidade.filme import Filme
from entidade.sala import Sala
from entidade.sessao import Sessao
from entidade.ingresso import Ingresso
from datetime import datetime

from enum import Enum

class MetodoDePagamento(Enum):
    DINHEIRO = "dinheiro"
    CARTAO_CREDITO = "cartão de crédito"
    CARTAO_DEBITO = "cartão de débito"


class Venda:
    def __init__(self, cliente: Cliente, ingressos: list[Ingresso], metodo_de_pagamento: MetodoDePagamento):
        self.cliente = cliente
        self.ingressos = ingressos
        self.metodo_de_pagamento = metodo_de_pagamento
        self.__data = datetime.now()
        self.__preco_total = self.calcular_preco_total()

    @property
    def cliente(self) -> Cliente:
        if not isinstance(self.__cliente, Cliente):
            raise TypeError("O cliente deve ser uma instância da classe Cliente.")
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("O cliente deve ser uma instância da classe Cliente.")
        self.__cliente = cliente

    @property
    def ingressos(self) -> list[Ingresso]:
        if not all(isinstance(ingresso, Ingresso) for ingresso in self.__ingressos):
            raise TypeError("Todos os itens de ingressos devem ser instâncias da classe Ingresso.")
        return self.__ingressos

    @ingressos.setter
    def ingressos(self, ingressos: list[Ingresso]):
        if not isinstance(ingressos, list) or not all(isinstance(ingresso, Ingresso) for ingresso in ingressos):
            raise TypeError("Ingressos deve ser uma lista de objetos do tipo Ingresso.")
        self.__ingressos = ingressos
        self.__preco_total = self.calcular_preco_total()

    @property
    def preco_total(self) -> float:
        if not isinstance(self.__preco_total, (int, float)):
            raise TypeError("O preço total deve ser um valor numérico.")
        return self.__preco_total

    @property
    def metodo_de_pagamento(self) -> MetodoDePagamento:
        if not isinstance(self.__metodo_de_pagamento, MetodoDePagamento):
            raise TypeError("O método de pagamento deve ser uma instância de MetodoDePagamento.")
        return self.__metodo_de_pagamento

    @metodo_de_pagamento.setter
    def metodo_de_pagamento(self, metodo_de_pagamento: MetodoDePagamento):
        if not isinstance(metodo_de_pagamento, MetodoDePagamento):
            raise TypeError("O método de pagamento deve ser uma instância de MetodoDePagamento.")
        self.__metodo_de_pagamento = metodo_de_pagamento

    @property
    def data(self) -> datetime:
        if not isinstance(self.__data, datetime):
            raise TypeError("A data deve ser uma instância de datetime.")
        return self.__data

    def calcular_preco_total(self) -> float:
        return sum(ingresso.preco for ingresso in self.__ingressos)

    def __str__(self):
        return (f"Venda para {self.cliente.nome} em {self.data.strftime('%d/%m/%Y %H:%M:%S')}.\n"
                f"Método de pagamento: {self.metodo_de_pagamento.value}\n"
                f"Total de ingressos: {len(self.ingressos)}\n"
                f"Preço total: R${self.preco_total:.2f}")
