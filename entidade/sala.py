class Sala:
    """
    Classe que representa o modelo de uma Sala no sistema.

    Atributos:
    - numero: Número da visao.
    - capacidade: Capacidade máxima de pessoas na visao.
    """

    def __init__(self, numero:int, capacidade:int):
        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(capacidade, int):
            self.__capacidade = capacidade

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        if isinstance(capacidade, int):
            self.__capacidade = capacidade
