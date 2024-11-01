class Sala:
    def __init__(self, numero:int, capacidade:int, tipo:str):
        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(capacidade, int):
            self.__capacidade = capacidade
        if isinstance(tipo, str):
             self.__tipo = tipo

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
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo