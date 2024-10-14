class SalaModelo:
    """
    Classe que representa o modelo de uma Sala no sistema.

    Atributos:
    - numero: Número da sala.
    - capacidade: Capacidade máxima de pessoas na sala.
    - tipo: Tipo da sala (ex: '2D', '3D', 'IMAX').
    """

    def __init__(self, numero, capacidade, tipo):
        self.__numero = numero
        self.__capacidade = capacidade
        self.__tipo = tipo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo
