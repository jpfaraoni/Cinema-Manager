from cliente import Cliente
from filme import Filme
from sala import Sala
from sessao import Sessao
from ingresso import Ingresso
from datetime import datetime

class Venda:
    def __init__(self, cliente: Cliente, ingressos: list[Ingresso], metodo_de_pagamento: str):
        self.__cliente = cliente
        self.__ingressos = ingressos  # Agora é uma lista de ingressos
        self.__metodo_de_pagamento = metodo_de_pagamento
        self.__data = datetime.now()  # Registra a data e hora da venda
        self.__preco_total = self.calcular_preco_total()

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @property
    def ingressos(self) -> list[Ingresso]:
        return self.__ingressos

    @ingressos.setter
    def ingressos(self, ingressos: list[Ingresso]):
        self.__ingressos = ingressos
        self.__preco_total = self.calcular_preco_total()  # Atualiza o total quando os ingressos mudam

    @property
    def preco_total(self) -> float:
        return self.__preco_total

    @property
    def metodo_de_pagamento(self) -> str:
        return self.__metodo_de_pagamento

    @metodo_de_pagamento.setter
    def metodo_de_pagamento(self, metodo_de_pagamento: str):
        self.__metodo_de_pagamento = metodo_de_pagamento

    @property
    def data(self) -> datetime:
